import logging
from odoo import models, fields, api,_
_logger = logging.getLogger(__name__)
from datetime import datetime, timedelta,date
from odoo.tools import html2plaintext
from odoo.fields import Date
from odoo.exceptions import ValidationError, UserError

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
    log_history = fields.Html(string='Log History', compute='_compute_log_history', store=False)

    @api.depends('message_ids.date', 'message_ids.body')
    def _compute_log_history(self):
        for lead in self:
            messages = self.env['mail.message'].search([
                ('model', '=', 'crm.lead'),
                ('res_id', '=', lead.id)
            ], order='date DESC')

            log_content = """
                    <style>
                        .log-container {
                            font-family: Arial, sans-serif;
                            background-color: #f9f9f9;
                            border: 1px solid #ddd;
                            border-radius: 8px;
                            padding: 15px;
                            max-height: 300px;
                            overflow-y: auto;
                        }
                        .log-item {
                            margin-bottom: 10px;
                            padding: 10px;
                            background-color: #fff;
                            border: 1px solid #eee;
                            border-radius: 4px;
                            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                        }
                        .log-date {
                            font-size: 12px;
                            color: #888;
                            margin-bottom: 5px;
                        }
                        .log-body {
                            font-size: 14px;
                            color: #333;
                        }
                    </style>
                    <div class="log-container">
                    """

            if messages:
                for msg in messages:
                    log_content += f"""
                            <div class="log-item">
                                <div class="log-date">{msg.date}</div>
                                <div class="log-body">{html2plaintext(msg.body)}</div>
                            </div>
                            """
            else:
                log_content += "<div class='log-item'>Tidak ada log.</div>"

            log_content += "</div>"
            lead.log_history = log_content


    @api.depends('calendar_event_ids.in_this_week')
    def _compute_has_meeting_this_week(self):
        for lead in self:
            lead.has_meeting_this_week = any(
                event.in_this_week
                for event in lead.calendar_event_ids
            )

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
        if self.env.user.has_group('sales_team.group_sale_manager'):
            self.write(
                {'state_lost_leads': 'approved'},
            )
        else:
            raise ValidationError(_("You do not have access to perform approval."))

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
