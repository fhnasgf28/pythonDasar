from odoo import models, fields, api


class DiscountProduct(models.Model):
    _inherit = 'product.template'

    @api.onchange('discount_apply_on')
    def _onchange_discount_apply_on(self):
        for program in self:
            if program.discount_apply_on == 'specific_products':
                program.discount_specific_product_ids = False
                categories = self.env['product.category'].search([])
                allowed_category_ids = []
                for cat in categories:
                    products = self.env['product.template'].search([('categ_id', '=', cat.id)])
                    if products:
                        allowed_category_ids.append(cat.id)
                return {
                    'domain': {
                        'discount_specific_product_ids': [('id', 'in', allowed_category_ids)]
                    }
                }