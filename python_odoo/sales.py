from odoo import models, fields, api, exceptions

class SalesOrderLine(models.Model):
    _inherit = 'sale.order.line'

    is_discounted = fields.Boolean(string='Discount Applied', default=False)

    @api.onchange('product_id', 'product_uom_qty')
    def _apply_discount(self):
        for line in self:
            line.discount = 0
            line.is_discount = False

            if line.product_id:
                discount_category = self.env['ir.config_parameter'].sudo().get_param('sales.discount_category_id')
                discount_threshold = int(self.env['ir.config_parameter'].sudo().get_param('sales.discount_threshold', 10))
                discount_percentage = float(
                    self.env['ir.config_parameter'].sudo().get_param('sales.discount_percentage', 5))

            if line.product_id.categ_id.id == int(discount_category) and line.product_uom_qty >= discount_threshold:
              line.discount = discount_percentage
              line.is_discount = True