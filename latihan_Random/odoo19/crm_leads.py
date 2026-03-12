from odoo import models, fields, api



class CrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.depends('user_id', 'type')
    def _compute_team_id(self):
        for lead in self:
            if not lead.user_id:
                continue
            user = lead.user_id
            if lead.team_id and user in (lead.team_id.member_ids| lead.team_id.user_id):
                continue
            team_domain = [('use_leads', '=', True)] if lead.type == 'lead' else [('use_opportunities', '=', True)]
            team = self.env['crm.team']._get_default_team_id(user.id, team_domain)
            if lead.team_id != team:
                lead.team_id = team.id 