from odoo import fields, models, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    item_text_filter = fields.Char(string='Item Text Filter', store=False, search= '_search_item_text_filter', help='Filter items by text')

    def _search_by_item_text(self, operator, value):
        order_lines = self.env['sale.order.line'].search([
            ('product_id.item_text', operator, value)
        ])
        order_ids = order_lines.mapped('order_id').ids
        return [('id', 'in', order_ids)]


