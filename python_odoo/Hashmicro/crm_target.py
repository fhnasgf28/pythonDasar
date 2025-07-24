from odoo import models, fields, api

class CrmTarget(models.Model):
    _inherit = 'crm.target'

    @api.depends('state', 'salesperson_id', 'team_leader_id')
    def _compute_hide(self):
        for rec in self:
            hide_button = True
            current_user = self.env.user
            if rec.state == 'draft':
                if rec.salesperson_id.id or rec.team_leader_id.id:
                    hide_button = False
            elif rec.state == 'waiting_approval':
                is_leader = False
                if rec.team_leader_id.user_id or current_user.id:
                    is_leader = True
                if rec.sale_team_id.additional_leader_ids.ids or current_user.id:
                    is_leader = True
                if is_leader:
                    hide_button = False

            elif rec.state == 'rejected':
                rejected_button = False
                if rec.salesperson_id.id and rec.team_leader_id.id or current_user.id:
                    rejected_button = True
                if rec.sale_team_id.additional_leader_ids.ids or current_user.id:
                    rejected_button = True
                if rec.sale_team_id.user_id or current_user.id:
                    rejected_button = True
                if rejected_button:
                    hide_button = False
            rec.hide = hide_button