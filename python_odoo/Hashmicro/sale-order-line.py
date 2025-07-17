from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.depends('purchase_price')
    def _compute_actual_cost(self):
        for line in self:
            if line.purchase_price:
                line.actual_cost = line.purchase_price
            else:
                line.actual_cost = 0.0
            
    @api.depends('purchase_price', 'product_uom_qty', 'price_subtotal')
    def _compute_margin(self):
        for line in self:
            line.margin = line.price_subtotal - (line.actual_cost * line.product_uom_qty)
            line.margin_percent = line.price_subtotal and line.margin / line.price_subtotal
    
    @api.onchange('line_warehouse_id_new')
    def set_price_from_pricelist(self):
        self.env.context = dict(self.env.context)
        for line in self:
            if self.line_warehouse_id_new:
                self.env.context.update({
                    'warehouse_id': self.line_warehouse_id_new.id,
                })
            line.product_uom_change()

    @api.depends('tax_id')
    def _compute_have_ppn(self):
        for line in self:
            have_ppn = False
            have_pph = False
            if line.tax_id:
                have_ppn = True if line.tax_id.filtered(lambda x: x.is_ppn) else False
                have_pph = True if line.tax_id.filtered(lambda x: x.is_pph) else False
            line.have_ppn = have_ppn
            line.have_pph = have_pph