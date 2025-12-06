from odoo import models, fields, api
import json

class StockScrapRequest(models.Model):
    _inherit = 'stock.scrap'

    @api.model
    def default_get(self, fields):
        res = super(StockScrapRequest, self).default_get(fields)
        self._get_usage_approve_button_from_config(res)
        return res

    @api.depends('branch_id')
    def _compute_location(self):
        if self.env.branches.ids:
            warehouse_ids = self.env['stock.warehouse'].search(
                [('branch_id', 'in', self.env.branches.ids), ('company_id', '=', self.env.company.id)])
            if warehouse_ids:
                self.domain_warehouse_id = json.dumps([('id', 'in', warehouse_ids.ids)])
            else:
                self.domain_warehouse_id = json.dumps([])
        else:
            self.domain_warehouse_id = json.dumps([])