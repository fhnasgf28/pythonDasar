from odoo import models, fields, api,_

class CalendarEventInherit(models.Model):
    _inherit = 'calendar.event'

    meeting_salesperson_ids = fields.Many2many('res.users', string='Salesperson', compute='_compute_meeting_salesperson_ids', store=True)
    is_hide_salesperson = fields.Boolean(string='Hide Salesperson', compute='_compute_is_hide_salesperson', store=False)
    dummy_boolean = fields.Many2many("DummyModel", compute="_compute_dummy_boolean", store=True)
    user_ids = fields.Many2many("res.users", 'user_calendar_rel', 'calendar_id','user_id', string='salesperson')
    mandatory = fields.Boolean('Mandatory')
    partner_attendees_ids = fields.Many2many(
        'res.partner', 'calendar_event_res_partner_rel', string='Other Attendees'
    )
    reasons_reschedule = fields.Char('Reasons Reschedule', readonly=True)

    @api.depends('opportunity_id')
    def _compute_salesperson(self):
        for res in self:
            is_multi_salesperson = self.env.user.id in self.env.ref('equip3_crm_operation.group_use_multi_salesperson_on_leads').users.ids
            partner_ids = []
            if self.opportunity_id:
                if is_multi_salesperson and self.opportunity_id.salesperson_lines:
                    for line in self.opportunity_id.salesperson_lines:
                        if line.salesperson_id.partner_id.user_ids:
                            partner_ids.append(line.salesperson_id.partner_id.user_ids[0].id)
                else:
                    partner_ids.append(res.opportunity_id.user_id.id)
                res.meeting_salesperson_ids = [(6, 0, partner_ids)]
            else:
                res.meeting_salesperson_ids = [(6, 0, self.env.user.ids)]


    @api.onchange('categ_ids')
    def set_mandatory(self):
        for res in self:
            if res.categ_ids:
                for i in res.categ_ids:
                    if i.leads_meeting:
                        res.mandatory = True
                        break

    @api.depends('user_id')
    def _compute_is_hide_salesperson(self):
        for i in self:
            is_multi_salesperson = self.env.user.id in self.env.ref('equip3_crm_operation.group_use_multi_salesperson_on_leads').users.ids
            if is_multi_salesperson:
                i.is_hide_salesperson = True
            else:
                i.is_hide_salesperson = False