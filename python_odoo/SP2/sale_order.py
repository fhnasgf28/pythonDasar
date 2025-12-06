from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    total_amount = fields.Float(string="Total Amount", compute='_compute_total_amount', store=True)

    @api.depends('order_line.price_subtotal')
    def _compute_total_amount(self):
        for record in self:
            record.total_amount = sum(
                [line.price_subtotal for line in record.order_line]
            )
