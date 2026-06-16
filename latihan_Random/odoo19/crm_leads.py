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
    
    @api.depends('team_id', 'type')
    def _compute_stage_id(self):
        for lead in self:
            if not lead.stage_id or (lead.team_id and lead.stage_id.team_ids and lead.team_id not in lead.stage_id.team_ids):
                lead.stage_id = lead._stage_find(domain=[('fold', '=', False)]).id 
    
    @api.depends('user_id')
    def _compute_date_open(self):
        for lead in self:
            if not lead.date_open and lead.user_id:
                lead.date_open = self.env.cr.now()
    
    @api.depends('stage_id')
    def _compute_date_last_stage_update(self):
        for lead in self:
            if not lead.date_last_stage_update:
                lead.date_last_stage_update = self.env.cr.now()

    @api.depends('partner_id')
    def _compute_function(self):