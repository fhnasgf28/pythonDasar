from odoo import models, fields, api,_ 
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    external_reference = fields.Char(string='External Reference')
    is_synced = fields.Boolean(string='Is Synced', default=False)
    total_amount = fields.Float(string='Total Amount', compute='_compute_total_amount', store=True)

    @api.model_create_multi
    def create(self, vals_list):
        records = super(SaleOrder, self).create(vals_list)
        for rec in records:
            if not rec.partner_id:
                raise UserError(_('Customer is required.'))
        return records
    
    def write(self, vals):
        res = super().write(vals)
        for rec in self:
            if rec.amount_total < 0:
                raise UserError(_('Total amount cannot be negative.'))
        return res
    
    def _compute_total_amount(self):
        for rec in self:
            rec.total_amount = sum(line.price_total for line in rec.order_line)
