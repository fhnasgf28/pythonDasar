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


