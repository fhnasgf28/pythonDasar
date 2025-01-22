import logging
from odoo import models, fields, api,_
_logger = logging.getLogger(__name__)
from datetime import datetime, timedelta,date
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
    has_meeting_this_week = fields.Boolean(string="Has Meeting This Week",compute="_compute_has_meeting_this_week", store=True)
    is_activity_today = fields.Boolean(string='is activity today', help="Indikator apakah lead memiliki aktivitas follow-up hari ini")
    is_activity_this_week = fields.Boolean(string='is activity this week',help="Indikator apakah lead memiliki aktivitas follow-up minggu ini")

    @api.depends('calendar_event_ids.in_this_week')
    def _compute_has_meeting_this_week(self):
        print('farhanassegaf akan maju')
        for lead in self:
            lead.has_meeting_this_week = any(
                event.in_this_week
                for event in lead.calendar_event_ids
            )

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
        # self.update_this_week_meeting()
        return super(CRMLead, self).write(vals)
    @api.depends('meeting_ids', 'meeting_ids.state')
    def _compute_first_meeting_date(self):
        print('farhanassegaf akan maju1')
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
        print('farhanassegaf akan maju3')
        """Helper method to dynamically fetch stage IDs by names."""
        stages = self.env['crm.stage'].search([('name', 'in', stage_names)])
        return stages.mapped('id')

    @api.depends('stage_id', 'first_meeting_date')
    def _compute_tracking_duration(self):
        print('farhanassegaf akan maju4')
        stage_ids = self._get_stage_ids(['(BD)WARM','(BD)FOCUS LEAD(MORE THAN 1 MEETING AND OWN TARGET)'])
        for lead in self:
            if lead.stage_id.id in stage_ids and lead.first_meeting_date:
                duration = (fields.Datetime.now() - lead.first_meeting_date).days
                lead.tracking_duration = duration
            else:
                lead.tracking_duration = 0
        print('kodingan ini', stage_ids)

    def _check_stage_and_update_meetings(self, vals):
        print('farhanassegaf akan maju5')
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
        print('farhanassegaf akan maju6')
        stage_ids = self._get_stage_ids(['(BD)WARM', '(BD)FOCUS LEAD(MORE THAN 1 MEETING AND OWN TARGET)'])
        going_to_meet = self._get_stage_ids(['(SA) GOING TO MEET'])
        for lead in self:
            previous_stage = lead.stage_id.id if lead.stage_id else None
            new_stage = vals.get('stage_id', previous_stage)
            if previous_stage in going_to_meet and new_stage in stage_ids:
                if lead.first_meeting_date:
                    duration = (fields.Datetime.now() - lead.first_meeting_date).days
                    lead.tracking_duration = duration

    # follow up leads per week or day
    def _check_activity_today(self, activity):
        if activity.date_deadline ==  Date.context_today(self):
            lead = self.env['crm.lead'].browse(activity.res_id)
            if lead:
                lead._get_leads_to_follow_up(time_range='day')

    def _get_leads_to_follow_up(self):
        """
        Perbarui field `has_activity_today` dan `has_activity_this_week`
        untuk semua leads.
        """
        print('farahnassegaf kodigan in ok')
        today = Date.context_today(self)
        print(today)
        start_week = today - timedelta(days=today.weekday())
        end_week = start_week + timedelta(days=6)
        # Reset flags
        self.search([]).write({'is_activity_today': False, 'is_activity_this_week': False})
        # Update flags for today
        mail_activity = self.env['mail.activity']
        activities_today = mail_activity.search([
            ('res_model', '=', 'crm.lead'),
            ('date_deadline', '=', today)
        ])
        print('activities today', activities_today)
        print(f"activities_today: {activities_today.mapped('display_name')}")
        leads_today = activities_today.mapped('res_id')
        print('leads today', leads_today)
        self.browse(leads_today).write({'is_activity_today': True})
        print('is_activity_today', self.is_activity_today)
        # Update flags for this week
        activities_week = mail_activity.search([
            ('res_model', '=', 'crm.lead'),
            ('date_deadline', '>=', start_week),
            ('date_deadline', '<=', end_week)
        ])
        print(f"activities_week: {activities_week.mapped('display_name')}")
        leads_week = activities_week.mapped('res_id')
        print('leads week', leads_week)
        self.browse(leads_week).write({'is_activity_this_week': True})

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
