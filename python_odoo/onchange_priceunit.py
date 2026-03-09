res_product_uom_qty = fields.Float("Product UoM Qty")

    @api.onchange('product_uom', 'product_uom_qty')
    def product_uom_change(self):
        price_unit = self.price_unit
        res = super().product_uom_change()
        self.price_unit = price_unit
        return res

    @api.onchange('product_uom')
    def convert_uom(self):
        for rec in self:
            if rec.product_id:
                if not rec.res_product_uom_qty:
                    rec.res_product_uom_qty = rec.product_uom_qty
                qty = rec.product_uom._compute_quantity(1, rec.product_id.uom_id, rounding_method='HALF-UP')
                rec.price_unit = (rec.price_unit / rec.res_product_uom_qty) * qty
                rec.res_product_uom_qty = qty
