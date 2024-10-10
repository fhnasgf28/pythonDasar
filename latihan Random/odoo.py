def unlink(self):
    for line in self:
        if line.order_id.is_booking:
            if line.product_id:
                product = line.product_id
                product.qty_available += line.product_uom_qty
    return super(SaleOrderLine, self).unlink()