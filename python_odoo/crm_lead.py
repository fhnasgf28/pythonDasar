import logging

from docutils.nodes import description
from odoo import models, fields, api,_
_logger = logging.getLogger(__name__)
from datetime import datetime, timedelta,date
from odoo.fields import Date
from odoo.exceptions import ValidationError, UserError
import requests
import json

class CRMLead(models.Model):
    _inherit = 'crm.lead'

    is_lost_leads = fields.Boolean(string="Is Lost", default=False)
    lost_reason_id = fields.Many2one('crm.lost.reason', string='Lost Reason')
    lost_description = fields.Text(string='Description')
    country_id = fields.Many2one('res.country', string='Country', required=True)
    approver_user_id = fields.Many2one('res.users', string='Approver', default=lambda self: self.env.user)
    state_lost_leads = fields.Selection([
        ('to_approve', 'To Approve'),
        ('approved', 'Approved')
    ], string="State", default='to_approve')
    first_meeting_date = fields.Datetime(string="First Meeting Date",compute="_compute_first_meeting_date",store=True,
                                         help="Date of the first meeting linked to this opportunity")
    tracking_duration = fields.Integer(string="Tracking Duration (Days)", compute="_compute_tracking_duration",
                                       store=True, help="Time duration (in days) from first meeting to stage change")
    calendar_event_ids = fields.One2many('calendar.event','res_id',string='Meetings',
        domain=lambda self: [('res_model', '=', self._name)])
    activity_type_name = fields.Char( string="Activity Type",compute="_compute_activity_details",store=True)
    date_deadline_activity = fields.Date(string="Activity Deadline",compute="_compute_activity_details",store=True)
    has_meeting_this_week = fields.Boolean(string="Has Meeting This Week",compute="_compute_has_meeting_this_week", store=True)
    is_activity_today = fields.Boolean(string='is activity today', help="Indicator whether the lead has a follow-up activity today")
    is_activity_this_week = fields.Boolean(string='is activity this week',help="Indicator whether the lead has a follow-up activity this week")
    attachment_ids = fields.Many2many('ir.attachment','res_id', string='Attachments',compute='_compute_attachment_ids',store=True,readonly=True)
    is_approval_matrix = fields.Boolean(string="Is Approval Matrix")
    industry_ai = fields.Char(string="Industry AI")

    @api.depends('attachment_ids',
                 'name', 'partner_id',
                 'activity_ids.attachment_ids')
    def _compute_attachment_ids(self):
        for lead in self:
            self._cr.execute("""
                SELECT id
                FROM ir_attachment
                WHERE res_model = %s AND res_id = %s
            """, ('crm.lead', lead.id))
            direct_attachments = [row[0] for row in self._cr.fetchall()]
            activity_attachments = lead.activity_ids.mapped('attachment_ids.id')
            all_attachments = list(set(direct_attachments + activity_attachments))
            lead.attachment_ids = [(6, 0, all_attachments)]

    @api.depends('calendar_event_ids.in_this_week')
    def _compute_has_meeting_this_week(self):
        for lead in self:
            lead.has_meeting_this_week = any(
                event.in_this_week
                for event in lead.calendar_event_ids
            )

    def fetch_modules_from_ai(self, description_text):
        url_modules = "https://kttx1ae.hashmicro.com/api/v1/check/modules"
        headers = {
            "Content-Type": "application/json"
        }
        payload_modules = {
            "ModulesName": description_text if description_text else "No Description",
            "ModulesList": "[ 'Manufacturing', 'CRM Module', 'Sales Module', 'Purchase Module', 'Construction Module', 'Inventory Module', 'HRM']"
        }

        try:
            response = requests.post(url_modules, headers=headers, data=json.dumps(payload_modules), timeout=10)
            response.raise_for_status()
            farhan = response.json()
            print(farhan)
            return response.json()  # Directly return the json dictionary

        except requests.exceptions.RequestException as e:
            print(f"Error fetching modules from AI: Request failed - {e}")
            return {}  # Return empty dict in case of API error

        except json.JSONDecodeError:
            print("Error decoding JSON response from AI Module API.")
            return {}  # Return empty dict if JSON decode fails

    def fetch_industry_from_ai(self, company_name):
        """
        Mengirim data partner_name dan quotation description ke Hashy AI
        dan mengembalikan industri yang sesuai.
        """
        url = "https://kttx1ae.hashmicro.com/api/v1/check/industries"
        headers = {
            "Content-Type": "application/json"
        }
        payload = {
            "CompanyName": company_name if company_name else "unknown Company",
            "Industries": "['Manufacturing', 'Retail', 'F&B', 'Services', 'IT']"
        }

        try:
            response = requests.post(url, headers=headers, data=json.dumps(payload), timeout=10)
            response.raise_for_status()
            data = response.json()
            valid_industry = data
            if "IndustryName" in valid_industry:
                industry_name = valid_industry["IndustryName"]
                return str(industry_name).strip()
        except requests.exceptions.RequestException as e:
            return "Unknown"

    def cron_update_industries_ai(self):
        self.update_industries_ai()

    def cron_update_modules_ai(self):
        self.update_modules_ai()

    def update_industries_ai(self):
        batch_size = 200
        offset = 0
        while True:
            leads = self.env['crm.lead'].search([('industry_ai', '=', False)], limit=batch_size, offset=offset)
            # Keluar dari loop jika tidak ada lagi data
            if not leads:
                break
            for lead in leads:
                if lead.partner_name:
                    industry_ai = self.fetch_industry_from_ai(lead.partner_name)
                    lead.write({'industry_ai': industry_ai})
            offset += batch_size
            self._cr.commit()
        return True

    def update_modules_ai(self):
        leads = self.search([('crm_module_id', '=', False),('crm_module_ids', '=', False)])
        for lead in leads:
            sale_orders = self.env['sale.order'].search([('opportunity_id', '=', lead.id)])
            if not sale_orders:
                print(f"Lead {lead.id}: No sale orders found, skipping module update.")  # Log if no sale order
                continue
            descriptions = []
            for order in sale_orders:
                for line in order.order_line:
                    if line.name:
                        descriptions.append(line.name)
            description_text = ', '.join(descriptions) if descriptions else ""
            suggested_modules_dict = self.fetch_modules_from_ai(description_text)  # Fetch module names from AI

            if suggested_modules_dict:
                module_names = [module_name for module_name, value in suggested_modules_dict.items() if value == 1]  # Get module names where value is 1
                module_records = self.env['crm.module'].search([('name', 'in', module_names)])
                print("modules recordsss",module_records)

                if module_records:
                    main_module = module_records[0] if module_records else False  # Basic logic: first module as main
                    other_modules = module_records[1:] if len(module_records) > 1 else module_records if len(module_records) == 1 else False

                    lead_vals = {}  # Dictionary to hold values to write to lead
                    if main_module:
                        lead_vals['crm_module_id'] = main_module.id
                        print(f"Lead {lead.id}: Main Module (AI) updated to: {main_module.name}")
                    if other_modules:
                        lead_vals['crm_module_ids'] = [(6, 0, other_modules.ids)]  # Update m2m field with module record IDs
                        print(f"Lead {lead.id}: Modules (AI) updated to: {[m.name for m in other_modules]}")
                    if lead_vals:  # Only write if there are values to update
                        lead.sudo().write(lead_vals)
                else:
                    print(f"Lead {lead.id}: No matching CRM Module records found in Odoo for AI suggested modules: {suggested_modules_dict}")
            else:
                print(f"Lead {lead.id}: No modules suggested by AI for description: '{description_text}'")  # Log if AI returns no suggestions

            print("CRM Module AI update process completed.")  # Logging completion of cron job
            return True

    @api.depends('activity_ids.date_deadline','activity_ids.activity_type_id')
    def _compute_activity_details(self):
        for lead in self:
            if lead.activity_ids:
                activity = lead.activity_ids.sorted('date_deadline')[0]
                lead.activity_type_name = activity.activity_type_id.name
                lead.date_deadline_activity = activity.date_deadline
            else:
                lead.activity_type_name = False
                lead.date_deadline_activity = False

    @api.model
    def create(self, vals):
        lead = super(CRMLead, self).create(vals)
        lead._compute_attachment_ids()
        lead.update_modules_ai()
        if lead.meeting_ids:
            lead.first_meeting_date = min(lead.meeting_ids.mapped('start'))
        return lead

    def write(self, vals):
        if 'stage_id' in vals:
            self._check_stage_and_update_meetings(vals)
            self.previous_stage_id(vals)
        return super(CRMLead, self).write(vals)

    @api.depends('meeting_ids', 'meeting_ids.state')
    def _compute_first_meeting_date(self):
        for lead in self:
            if lead.meeting_ids:
                done_meetings = lead.meeting_ids.filtered(lambda m: m.state_5 == 'done' or m.state_5 == 'meeting')
                if len(done_meetings) == 1:
                    lead.first_meeting_date = done_meetings.start_date if done_meetings.allday else done_meetings.start
                else:
                    lead.first_meeting_date = False
            else:
                lead.first_meeting_date = False

    def _get_stage_ids(self, stage_names):
        """Helper method to dynamically fetch stage IDs by names."""
        stages = self.env['crm.stage'].search([('name', 'in', stage_names)])
        return stages.mapped('id')

    @api.depends('stage_id', 'first_meeting_date')
    def _compute_tracking_duration(self):
        stage_ids = self._get_stage_ids(['(BD)WARM','(BD)FOCUS LEAD(MORE THAN 1 MEETING AND OWN TARGET)'])
        for lead in self:
            if lead.stage_id.id in stage_ids and lead.first_meeting_date:
                duration = (fields.Datetime.now() - lead.first_meeting_date).days
                lead.tracking_duration = duration
            else:
                lead.tracking_duration = 0

    def _check_stage_and_update_meetings(self, vals):
        stage_ids = self._get_stage_ids(['(BD)WARM','(BD)FOCUS LEAD(MORE THAN 1 MEETING AND OWN TARGET)'])
        if not stage_ids:
            return
        new_stage_id = vals.get('stage_id')
        for lead in self:
            old_stage_id = lead.stage_id.id if lead.stage_id else None
            if new_stage_id in stage_ids and new_stage_id != old_stage_id:
                self.calendar_event_ids._cron_update_meeting_status()
                break

    def previous_stage_id(self, vals):
        stage_ids = self._get_stage_ids(['(BD)WARM', '(BD)FOCUS LEAD(MORE THAN 1 MEETING AND OWN TARGET)'])
        going_to_meet = self._get_stage_ids(['(SA) GOING TO MEET'])
        for lead in self:
            previous_stage = lead.stage_id.id if lead.stage_id else None
            new_stage = vals.get('stage_id', previous_stage)
            if previous_stage in going_to_meet and new_stage in stage_ids:
                if lead.first_meeting_date:
                    duration = (fields.Datetime.now() - lead.first_meeting_date).days
                    lead.tracking_duration = duration

    def action_open_activity_popup(self):
        self.ensure_one()
        self._compute_attachment_ids()
        return {
            'name': 'Logs and Activities',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'crm.lead',
            'res_id': self.id,
            'view_id': self.env.ref('crminternal_ktt_modifier.view_crm_lead_popup_form').id,
            'target': 'new',
            'context': {
                'form_view_initial_mode': 'readonly',
                'create': False,
                'edit': False,
            }
        }

    def _cron_get_leads_to_follow_up(self):
        query = """
                SELECT res_id
                FROM mail_activity
                WHERE res_model = 'crm.lead'
          """
        self.env.cr.execute(query)
        activity_res_ids = [res_id[0] for res_id in self.env.cr.fetchall()]
        if activity_res_ids:
            leads = self.browse(activity_res_ids)
            leads._get_leads_to_follow_up()

    def _get_leads_to_follow_up(self):
        """
        Perbarui field `is_activity_today` dan `is_activity_this_week`
        untuk semua leads.
        """
        today = Date.context_today(self)
        start_week = today - timedelta(days=today.weekday())
        end_week = start_week + timedelta(days=6)
        # query untuk mengambil aktivitas
        query = """
            SELECT res_id, date_deadline 
            FROM mail_activity
            WHERE res_model = 'crm.lead' AND res_id = ANY(%s)
        """
        self.env.cr.execute(query, (self.ids,))
        activities = self.env.cr.fetchall()
        # memisahkan activitas berdasaran tanggal
        activities_today_ids = {res_id for res_id, date in activities if date == today}
        activities_week_ids = {res_id for res_id, date in activities if start_week <= date <= end_week}
        for lead in self:
            lead_values = {
                'is_activity_today': lead.id in activities_today_ids,
                'is_activity_this_week': lead.id in activities_week_ids
            }
            lead.write(lead_values)

    def action_approve_lost(self):
        for lead in self:
            approval_matrix = self.env["crm.lost.approval.matrix"].search([
                ('company_id', '=', lead.company_id.id),
            ])
            if not approval_matrix:
                raise ValidationError(_("Approval Matrix has not been configured. Please configure it first."))
            lead.is_approval_matrix = any(self.env.user in matrix.approver_matrix_line_ids.user_name_ids for matrix in approval_matrix)
            self.write(
                {'state_lost_leads': 'approved'},
            )

    @api.model
    def update_leads_quotation_count(self):
        """
        Updates the quotation_count field for all leads.
        Only considers sale orders in states 'draft' or 'send'.
        """
        query = """
            UPDATE crm_lead cl
            SET quotation_counts = (
                SELECT COUNT(so.id)
                FROM sale_order so
                WHERE so.opportunity_id = cl.id
                AND so.state IN ('draft', 'send')
            )
            WHERE cl.id IN (
                SELECT id FROM crm_lead WHERE quotation_counts = 0
            );
        """
        self.env.cr.execute(query)
        self.env.cr.commit()

    def find_leads_similar(self, name,website='',email_from='',phone='',mobile='',partner_name='',my_id=False):
        where_params = ''
        id_params = ''
        query = """
            SELECT id, name
            FROM crm_lead
            WHERE lower(name) = lower('{}'){}
        """
        if partner_name:
            where_params += " or name = '{}'".format(name)
        if email_from:
            where_params += " or email_from = '{}'".format(email_from)
        if phone:
            where_params += " or phone = '{}'".format(phone)
        if mobile:
            where_params += " or mobile = '{}'".format(mobile)
        if partner_name:
            where_params += " or partner_name = '{}'".format(partner_name)
        if my_id:
            id_params += " and id != {}".format(my_id)
        self.env.cr.execute(query.format(name, where_params, id_params))
        query_result = self.env.cr.dictfetchall()
        return query_result

    def _compute_activity_count(self):
        for res in self:
            self.env.cr.execute("""
                SELECT COUNT(*) FROM res_mail_activity
                WHERE res_id = %s
            """, (res.id,))
            res.activity_count = self.env.cr.fetchone()[0]

    def _compute_meeting_count(self):
        if not self.ids:
            return

        opportunity_ids = tuple(self.ids)
        self.env.cr.execute("""
            SELECT opportunity_id, COUNT(*) FROM
            calendar_event 
            WHERE state IN ('meeting', 'done') AND opportunity_id IN %s
            GROUP BY opportunity_id
        """, (opportunity_ids,))
        # hasil query dikonversi menjadi dictionary
        meeting_counts = dict(self.env.cr.fetchall())

        for res in self:
            count = meeting_counts.get(res.id, 0)
            res.sudo().meeting_count = count
            res.sudo().meeting_count_2 = count
        # panggil methode lainnya
        self.compute_bd_intern()
        self._compute_check_group_user()

    def _compute_user_id(self):
        query = """
            UPDATE crm_lead 
            SET user_id = %s
            WHERE user_id IS NULL
        """
        self.env.cr.execute(query, (2,))

    def schedule_activity(self):
        for res in self:
            context = dict(self.env.context) or {}
            self.env.cr.execute("""
                SELECT id FROM ir_model WHERE model = %s LIMIT 1
            """, ('crm.lead',))
            result = self.env.cr.fetchone()
            model_id = result[0] if result else False

            if model_id:
                context.update({'res_model_id': model_id})
                return {
                    'type': 'ir.actions.act_window',
                    'name': 'Schedule Activity',
                    'view_type': 'form',
                    'view_mode': 'form',
                    'res_model': 'mail.activity',
                    'context': context,
                    'target': 'new',
                }

    @api.depends('order_ids.state', 'order_ids.currency_id', 'order_ids.amount_untaxed', 'order_ids.date_order',
                 'order_ids.company_id')
    def _compute_sale_data(self):
        res = super(CRMLead, self)._compute_sale_data()
        quotation_amount_model = self.env['quotation.amount']
        for rec in self:
            order_ids = [order.id for order in rec.order_ids]
            if order_ids:
                self.env.cr.execute("""
                        SELECT order_id
                        FROM quotation_amount
                        WHERE order_id in %s
                        """, (tuple(order_ids),))

                existing_order_ids = {row[0] for row in self.env.cr.fetchall()}
                new_order_ids = set(order_ids) - existing_order_ids

                if new_order_ids:
                    quotation_amount_model.create([
                        {'order_id': order_id} for order_id in new_order_ids
                    ])

            rec.sudo().quotation_counts = rec.quotation_count
        return res

    def action_sub_quotation(self):
        if self.partner_id:
            vals = ({
                'default_partner_id':self.partner_id.id,
                'default_team_id': self.team_id.id,
                'default_campaign_id': self.campaign_id.id,
                'default_medium_id': self.medium_id.id,
                'default_source_id': self.source_id.id,
                'default_opportunity_id': self.id,
                'default_user_id': self.user_id.id if self.env.user.has_group("crminternal_modifier.crm_group_intern_bd") and not self.env.user.has_group("crminternal_modifier.crm_group_bd_staff") else self.env.user.id,
                'default_is_subs_order': True,
            })
        else:
            raise UserError('In order to create sale order, Customer field should not be empty!')
        return {
            'name': "Create New Subs. Quotation",
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'sale.order',
            'target': 'current',
            'context': vals,
        }

class CrmLeadLost(models.TransientModel):
    _inherit = 'crm.lead.lost'
    _description = 'Get Lost Reason'

    description = fields.Text(string='Description', required=True)

    def action_lost_reason_apply(self):
        leads = self.env['crm.lead'].browse(self.env.context.get('active_ids'))
        if not self.lost_reason_id or not self.description:
            raise ValidationError("Please fill in both the lost reason and description before applying.")

        for lead in leads:
            lead.write({
                'lost_reason_id': self.lost_reason_id.id,
                'lost_description': self.description,
                'is_lost_leads': True,
            })

        return leads.action_set_lost(lost_reason=self.lost_reason_id.id)
