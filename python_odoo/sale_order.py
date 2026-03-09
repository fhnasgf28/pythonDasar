from odoo import api, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_create_rfq(self):
        for rec in self:
            rfq = self.env['sale.order'].create({
                'partner_id': rec.partner_id.id,
                'date_order': rec.date_order,
                'origin': rec.name,
                'order_line': [(0, 0, {
                    'product_id': line.product_id.id,
                    'name': line.name,
                    'product_qty': line.product_uom_qty,
                    'price_unit': line.price_unit,
                    'date_planned': fields.Datetime.now(),
                }) for line in rec.order_line]
            })
            return {
                'name': 'RFQ Created',
                'type': 'ir.actions.act_window',
                'res_model': 'sale.order',
                'view_mode': 'form',
                'res_id': rfq.id
            }
