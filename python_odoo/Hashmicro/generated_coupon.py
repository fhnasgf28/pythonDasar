from odoo import models, fields, api

class GeneratedCoupon(models.Model):
    _inherit = 'sale.order'

    def _generate_coupon(self):
        for order in self:
            order.coupon_id = self.env['coupon.coupon'].create({
                'name': order.name,
                'code': order.name,
                'discount': order.amount_untaxed * 0.1,
            })

    def _cancel_generated_coupon(self):
        for rec in self:
            if rec.applied_coupon_ids:
                rec.applied_coupon_ids.state = 'new'
                rec.order_line.filtered(lambda x: x.is_coupon).unlink()
            if rec.generated_coupon_ids:
                rec.generated_coupon_ids.state = 'cancel'
            rec.send_coupon_program_ids = [(6,0,[])]
            rec.coupon_ids = [(6,0,[])]

    def _create_reward_line_equip(self, program, qty, price_unit):
        self.ensure_one()
        order = self
        multiple_do_date_new = fields.datetime.now()
        warehouse_new_id = self.warehouse_new_id.id
        if self.is_single_delivery_date:
            multiple_do_date_new = self.commitment_date
        if program.reward_type == 'product':
            product_line = order.order_line.filtered(lambda l: l.product_id == program.reward_product_id)
            taxes = product_line.mapped('taxes_id').filtered(lambda t: t.company_id == order.company_id)
            line_to_add = [(0, 0, {
                'sale_line_sequence': str(len(order.order_line) + 1),
                'product_id': program.discount_line_product_id.id,
                'price_unit': 0,
                'product_uom_qty': qty,
                'is_reward_line': True,
                'name': program.name,
                'product_uom': program.reward_product_id.uom_id.id,
                'tax_id':[(4, tax.id, False) for tax in taxes],
                'account_tag_ids':[(6,0, order.account_tag_ids.ids)],
                'delivery_address_id': order.partner_id.id,
                'multiple_do_date_new': multiple_do_date_new,
                'line_warehouse_id_new': warehouse_new_id,
                'is_promotion_product_line': True
            })]
            line_to_update = [
                (1, line.id, {
                    'reward_quantity': qty,
                    'product_uom_qty': line.product_uom_qty + qty,
                })
                for line in order.order_line.filtered()
            ]


