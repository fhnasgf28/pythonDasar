from odoo import api, fields, models, _
from odoo.exceptions import UserError, AccessError

class CrmLeads(models.Model):
    _name = 'crm.lead.new'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True)
    lost_request_state = fields.Selection([
        ('none', 'None'),
        ('to_approve', 'To Approve'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], default='none', tracking=True)

    lost_requested_by_id = fields.Many2one('res.users', string="Lost Requested By", readonly=True)
    lost_approver_id = fields.Many2one('res.users', string="Lost Approver", readonly=True)
    lost_reason = fields.Text(string="Lost Reason")

    def _get_sales_leader(self):
        self.ensure_one()
        if not self.team_id:
            return False
        return self.team_id.user_id

    def action_request_lost(self):
        for rec in self:
            leader = rec._get_sales_leader()
            if not leader:
                raise UserError(_("Sales Leader belum di set disales team (%s)") % (rec.team_id.display_name or '-'))
            rec.write({
                'lost_request_state': 'to_approve',
                'lost_requested_by_id': self.env.user.id,
                'lost_approver_id': leader.id,
            })
            activity_type = self.env.ref('mail.mail_activity_data_todo')
            rec.activity_schedule(
                activity_type_id=activity_type.id,
                user_id=leader.id,
                summary=_("Approver Lost Request"),
                note=_("Ada request Lost dari %s.\nReason: %s") % (rec.name, rec.lost_reason or '-')
            )
            rec.message_post(body=_("Lost request diajukan ke Sales Leader: <b>%s</b>.") % leader.name)

            return True

    def _check_is_sales_leader(self):
        self.ensure_one()
        leader = self._get_sales_leader()
        if not leader or self.env.user.id != leader.id:
            raise AccessError(_("Hanya sales leader (Team Leader) yang boleh approve/reject"))