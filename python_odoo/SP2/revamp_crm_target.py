from odoo import models, fields, api

class CrmTarget(models.Model):
    _inherit = 'crm.target'

    target_amount = fields.Float('Target Amount', default=0.0)

    @api.depends('main_target', 'current_achievement')
    def _compute_target_left(self):
        for rec in self:
            target_left = rec.main_target
            if rec.current_achievement:
                target_left -= rec.current_achievement
            rec.target_left = target_left

    @api.model
    def create(self, vals):
        res = super(CrmTarget, self).create(vals)
        res.name = self.env['ir.sequence'].next_by_code('crm.target.seq') or _('New')
        return res

    def button_reject(self):
        for rec in self:
            rec.state = 'rejected'

    @api.depends('state')
    def _compute_hide(self):
        for rec in self:
            hide = False
            current_user = self.env.user.id
            if rec.state == 'draft':
                if current_user != rec.salesperson_id.id:
                    hide = True
            elif rec.state == 'waiting_approval':
                if current_user != rec.team_leader_id.id:
                    hide = True
            elif rec.state == 'rejected':
                if current_user != rec.salesperson_id.id and current_user != rec.team_leader_id.id:
                    hide = True
            rec.hide = hide

