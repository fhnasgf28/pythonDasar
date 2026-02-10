from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError, warning

class CrmPhonecall(models.Model):
    _inherit = 'crm.phonecall'

    feedback = fields.Text('Feedback')
    from_logged_calls = fields.Boolean(string='From Logged Calls', compute='_compute_from_logged_calls', store=True,help="Technical field to determine if the call was opened from logged calls view")
    activity_id = fields.Many2one('mail.activity', string='Activity')

    @api.depends('company_id')
    def _compute_from_logged_calls(self):
        from_logged_calls = self.env.context.get('from_logged_calls', False)
        for record in self:
            record.from_logged_calls = from_logged_calls

    def cancel_call(self):
        self.ensure_one()
        if self.state == 'open':
            self.state = 'cancel'
            self.activity_id.action_cancel()

    def hold_call(self):
        self.ensure_one()
        for rec in self:
            if rec.state == 'open':
                rec.state = 'pending'
                rec.write({'save_duration': rec.duration})

    def done_call(self):
        self.ensure_one()
        for rec in self:
            if rec.state == 'open':
                return {
                    'name':_('Call Feedback'),
                    'res_model': 'crm.phonecall.feedback.wizard',
                    'type': 'ir.actions.act_window',
                    'view_mode': 'form',
                    'target': 'new',
                    'context': {'default_phonecall_id': rec.id},
                    'flags': {'form': {'action_buttons': True}}
                }
            else:
                if rec.state == 'open':
                    rec.state = 'done'

    @api.model
    def create(self, vals):
        if self.env.context.get('from_logged_calls', False):
            vals = dict()
            vals['state'] = 'done'
            return super(CrmPhonecall, self).create(vals)

    def _action_delete_with_wizard(self, record):
        deleted = record.filtered(lambda x: x.state not in ('open', 'cancel', 'pending', 'done'))
        not_draft = record - deleted
        if not deleted:
            raise ValidationError(_("No record to delete"))

        if not_draft:
            return {
                'name': _('Delete Phone Call'),
                'type': 'ir.actions.act_window',
                'view_mode': 'form',
                'res_model': 'record.crm.delete',
                'view_id': self.env.ref('equip3_crm_operation.record_crm_delete_form_view').id,
                'target': 'new',
                'context': {
                    'default_phonecall_ids': not_draft.ids,
                    'default_phonecall_deleted_ids': deleted.ids,
                }
            }
        else:
            deleted.unlink()

    def action_make_meeting(self):
        res = super().action_make_meeting()
        res["context"].update({
            "default_meeting_salesperson_ids": [(6,0,self.env.user.ids)]
        })
        return res