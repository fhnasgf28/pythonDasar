from odoo import models, fields, api

class GetRewardValuesDiscount(models.Model):
    _inherit = 'sale.order'

    def _get_reward_values_discount(self, program):
        if program.discount_type == 'fixed_amount':
            taxes = program.dicount_line_product_id.taxes_id
            if self.fiscal_position_id:
                taxes = self.fiscal_position_id.map_taxes(taxes)
            return [{
                'name': program.name,
                'product_id': program.dicount_line_product_id.id,
                'product_uom_qty': 1,
                'price_unit': - self._get_reward_values_discount_fixed_amount(program),
                'is_reward_line':True,
                'tax_id': [(4, tax.id, False) for tax in taxes],
                'product_uom': program.discount_line_product_id.uom_id.id,
            }]
        reward_dict = {}
        lines = self._get_paid_order_lines()
        amount_total = sum(self._get_base_order_lines(program).mapped('price_subtotal'))
        if program.discount_apply_on == 'cheapset_product':
            line = self._get_cheapest_product()
            if line:
                discount_line_amount = min(line.price_reduct * (program.discount_percentage / 100), amount_total)
                if discount_line_amount:
                    taxes = self.fiscal_position_id.map_tax(line.tax_id)
                    reward_dict[line.tax_id] = {
                        'name': _("Discount: %(program)s - On product with following taxes: %(taxes)s", program=program.name, taxes=", ".join(taxes.mapped('name'))),
                        'product_id': program.discount_line_product_id.id,
                        'price_unit': - discount_line_amount if discount_line_amount > 0 else 0,
                        'product_uom_qty': 1,
                        'product_uom': program.discount_line_product_id.uom_id.id,
                        'is_reward_line': True,
                        'tax_id': [(4, tax.id, False) for tax in taxes],
                    }
        elif program.discount_apply_on in ['specific_products', 'specific_brands', 'specific_product_category']:
            if program.discount_apply_on == 'specific_products':
                lines = lines.filtered(lambda x: x.product_id in program.discount_specific_product_ids)
            elif program.discount_apply_on == 'specific_brands':
                lines = lines.filtered(lambda x: x.product_id.product_brand_ids in program.discount_specific_brand_ids)
            elif program.discount_apply_on == 'specific_product_category':
                lines = lines.filtered(lambda x: x.product_id.categ_id in program.discount_specific_product_category_ids)
            for line in lines:
                if line.is_reward_line:
                    continue
                discount_line_amount = min(self._get_reward_values_discount_percentage_per_line(program, line), amount_total)
                if discount_line_amount:
                    if line.tax_id in reward_dict:
                        reward_dict[line.tax_id]['price_unit'] -= discount_line_amount
                    else:
                        taxes = self.fiscal_position_id.map_tax(line.tax_id)
                        reward_dict[line.tax_id] = {
                            'name': _("Discount: %(program)s - On product with following taxes: %(taxes)s", program=program.name, taxes=", ".join(taxes.mapped('name'))),
                            'product_id': program.discount_line_product_id.id,
                            'price_unit': - discount_line_amount if discount_line_amount > 0 else 0,
                            'product_uom_qty': 1,
                            'product_uom': program.discount_line_product_id.uom_id.id,
                            'is_reward_line': True,
                            'tax_id': [(4, tax.id, False) for tax in taxes],
                        }
