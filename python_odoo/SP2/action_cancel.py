from odoo import fields, models, api
from odoo.exceptions import ValidationError


class ActionCancel(models.Model):
    _inherit = 'sale.order'

    def action_cancel(self):
        for record in self:
            if record.state == 'sale':
                picking_ids = record.picking_ids
                invoice_ids = record.order_line.mapped('invoice_lines.move_id')
                if invoice_ids and any(invoice.state == 'posted' for invoice in invoice_ids) and \
                    picking_ids and any(picking.state == 'done' for picking in picking_ids):
                    raise ValidationError('You Cannot Cancel Confirmed SO!')
                elif invoice_ids and any(invoice.state == 'draft' for invoice in invoice_ids):
                    raise ValidationError('There is an unfinish invoice. Please cancel the invoice first!')
                else:
                    if picking_ids and any(picking.state == 'done' for picking in picking_ids):
                        raise ValidationError("You can't cancel Delivered SO!")
                    elif picking_ids and any(picking.state not in ('done', 'cancel', 'rejected') for picking in picking_ids):
                        raise ValidationError("There is an unfinish delivery order. Please cancel DO first!")
                    else:
                        record.write({'state': 'cancel', 'sale_state': 'cancel', 'is_quotation_cancel': False})
            else:
                record.write({'state': 'cancel', 'sale_state': 'cancel', 'is_quotation_cancel': True})


    def _get_reward_values_discount(self, program):
        print("program", program)
        print("Mas Farhan kodingan ini di eksekusi tau ga sih kam uahaahhhh")
        if program.discount_type == 'fixed_amount':
            taxes = program.discount_line_product_id.taxes_id
            if self.fiscal_position_id:
                taxes = self.fiscal_position_id.map_tax(taxes)
            return [{
                'name': _("Discount: %s", program.name),
                'product_id': program.discount_line_product_id.id,
                'price_unit': - self._get_reward_values_discount_fixed_amount(program),
                'product_uom_qty': 1.0,
                'product_uom': program.discount_line_product_id.uom_id.id,
                'is_reward_line': True,
                'tax_id': [(4, tax.id, False) for tax in taxes],
            }]
        reward_dict = {}
        lines = self._get_paid_order_lines()
        amount_total = sum(self._get_base_order_lines(program).mapped('price_subtotal'))
        if program.discount_apply_on == 'cheapest_product':
            line = self._get_cheapest_line()
            if line:
                discount_line_amount = min(line.price_reduce * (program.discount_percentage / 100), amount_total)
                if discount_line_amount:
                    taxes = self.fiscal_position_id.map_tax(line.tax_id)

                    reward_dict[line.tax_id] = {
                        'name': _("Discount: %s", program.name),
                        'product_id': program.discount_line_product_id.id,
                        'price_unit': - discount_line_amount if discount_line_amount > 0 else 0,
                        'product_uom_qty': 1.0,
                        'product_uom': program.discount_line_product_id.uom_id.id,
                        'is_reward_line': True,
                        'tax_id': [(4, tax.id, False) for tax in taxes],
                    }
        elif program.discount_apply_on in ['specific_products', 'on_order', 'specific_brands', 'specific_product_category']:
            if program.discount_apply_on == 'specific_products':
                # We should not exclude reward line that offer this product since we need to offer only the discount on the real paid product (regular product - free product)
                free_product_lines = self.env['coupon.program'].search([('reward_type', '=', 'product'),
                                                                        ('reward_product_id', 'in',
                                                                         program.discount_specific_product_ids.ids)]).mapped(
                    'discount_line_product_id')
                lines = lines.filtered(
                    lambda x: x.product_id in (program.discount_specific_product_ids | free_product_lines))
            elif program.discount_apply_on == 'specific_brands':
                lines = lines.filtered(lambda x: x.product_id.product_brand_ids in program.discount_specific_brand_ids)
            elif program.discount_apply_on == 'specific_product_category':
                # Filter lines based on product category
                lines = lines.filtered(lambda x: x.product_id.categ_id in program.discount_specific_product_category_ids)
                print("lines", lines)
                print(program.discount_specific_product_category_ids)
            # when processing lines we should not discount more than the order remaining total
            currently_discounted_amount = 0
            for line in lines:
                if line.is_reward_line:
                    continue
                discount_line_amount = min(self._get_reward_values_discount_percentage_per_line(program, line),
                                           amount_total - currently_discounted_amount)

                if discount_line_amount:

                    if line.tax_id in reward_dict:
                        reward_dict[line.tax_id]['price_unit'] -= discount_line_amount
                    else:
                        taxes = self.fiscal_position_id.map_tax(line.tax_id)

                        reward_dict[line.tax_id] = {
                            'name': _(
                                "Discount: %(program)s - On product with following taxes: %(taxes)s",
                                program=program.name,
                                taxes=", ".join(taxes.mapped('name')),
                            ),
                            'product_id': program.discount_line_product_id.id,
                            'price_unit': - discount_line_amount if discount_line_amount > 0 else 0,
                            'product_uom_qty': 1.0,
                            'product_uom': program.discount_line_product_id.uom_id.id,
                            'is_reward_line': True,
                            'tax_id': [(4, tax.id, False) for tax in taxes],
                        }
                        currently_discounted_amount += discount_line_amount

        # If there is a max amount for discount, we might have to limit some discount lines or completely remove some lines
        max_amount = program._compute_program_amount('discount_max_amount', self.currency_id)
        if max_amount > 0:
            amount_already_given = 0
            for val in list(reward_dict):
                amount_to_discount = amount_already_given + reward_dict[val]["price_unit"]
                if abs(amount_to_discount) > max_amount:
                    reward_dict[val]["price_unit"] = - (max_amount - abs(amount_already_given))
                    add_name = formatLang(self.env, max_amount, currency_obj=self.currency_id)
                    reward_dict[val]["name"] += "( " + _("limited to ") + add_name + ")"
                amount_already_given += reward_dict[val]["price_unit"]
                if reward_dict[val]["price_unit"] == 0:
                    del reward_dict[val]
        vals = list(reward_dict.values())
        if program.discount_apply_on == 'on_order':
            total_price_unit = sum(item['price_unit'] for item in vals)
            if vals:
                vals[0]['price_unit'] = total_price_unit
        return vals