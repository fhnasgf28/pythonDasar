from datetime import datetime, timedelta
from odoo import models, fields, api
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def get_last_week_orders(self):
        today = fields.Date.today()
        last_week = today - timedelta(days=7)
        orders = self.search([('date_order', '>=', last_week), ('date_order', '=', today)])
        return orders
    
    @api.model
    def get_orders_by_customer(self):
        customer = self.env['res.partner'].search([('name', '=', 'PT Mandiri Utama')], limit=1)
        if customer:
            orders = self.search([('partner_id', '=', customer.id)])
            return orders
        return self.browse([])
    
    @api.model
    def get_orders_by_product(self):
        product = self.env["product.product"].search([('name', '=', 'Product A')], limit=1)
        if product:
            lines = self.env["sale.order.line"].search([('product_id', '=', product.id)])
            order_ids = lines.mapped('order_id')
            return order_ids
        return self.env["sale.order"].browse([])
    