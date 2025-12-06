from odoo import models, fields, api, _
from pydantic import ValidationError


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    @api.constrains('probability', 'stage_id')
    def _check_won_validity(self):
        for lead in self:
            if lead.stage_id.is_won and lead.probability !=  100:
                raise ValidationError(_("The probability of a won lead must be 100"))

    @api.depends('company_id')
    def _compute_user_company_ids(self):
        all_companies = self.env['res.company'].search([])
        for lead in self:
            if not lead.company_id:
                lead.user_company_ids  = all_companies
            else:
                lead.user_company_ids = lead.company_id

    @api.depends('company_id')
    def _compute_company_currency(self):
        for lead in self:
            if not lead.company_id:
                lead.company_currency = self.env.company.currency_id
            else:
                lead.company_currency = lead.company_id.currency_id

    @api.depends('user_id', 'type')
    def _compute_team_id(self):
        for lead in self:
            proposal = lead.company_id
            if proposal:
                if lead.user_id and proposal not in lead.user_id.company_id:
                    proposal = False
                elif lead.team_id.company_id and proposal != lead.team_id.company_id:
                    proposal = False
                elif lead.team_id and not lead.team_id.company_id and not lead.user_id:
                    proposal = False
                elif not lead.team_id and not lead.user_id and \
                        (not lead.partner_id or lead.partner_id.company_id != proposal):
                    proposal = False
            if not proposal:
                if lead.team_id.company_id:
                    lead.company_id = lead.team_id.company_id
                elif lead.user_id:
                    if self.env.company in lead.user_id.company_ids:
                        lead.company_id = self.env.company
                    else:
                        lead.company_id = lead.user_id.company_id & self.env.companies
                elif lead.partner_id:
                    lead.company_id = lead.partner_id.company_id
                else:
                    lead.company_id = False

    @api.depends('team_id', 'type')
    def _compute_stage_id(self):
        for lead in self:
            if not lead.stage_id:
                lead.stage_id = self._stage_find(domain=[('fold', '=', False)]).id



