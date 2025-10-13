def copy(self, default=None):
    if default is None:
        default = {}
    new_mr = super(MaterialRequest, self).copy(default)
    for line in self.product_line:
        if line.product:
            self.env['material.request.line'].create({
                'material_request_id': new_mr.id,
                'product': line.product.id,
                'quantity': line.quantity,
                'destination_warehouse_id': line.destination_warehouse_id.id if line.destination_warehouse_id else False,
                'product_unit_measure': line.product_unit_measure.id,
                'description': line.description or '',
            })

    return new_mr
