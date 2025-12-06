from odoo import models, fields, api

class CrmTarget(models.Model):
    _name = "crm.target"
    _description = "CRM Target"

    target_count = fields.Integer(string="Total Targets", compute="_compute_target_count")

    @api.depends()
    def _compute_target_count(self):
        total = self.env['crm.target'].search_count([])
        for record in self:
            record.target_count = total
