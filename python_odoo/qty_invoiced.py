@api.depends('invoice_lines.move_id.state', 'invoice_lines.quantity', 'qty_received', 'product_uom_qty', 'order_id.state')
    def _compute_qty_invoiced(self):
        print("kodingan ini mantep banget seprtinya nih")
        for line in self:
            qty = 0.0
            for inv_line in line.invoice_lines:
                if inv_line.move_id.state not in ['cancel', 'rejected']:
                    if inv_line.move_id.move_type == 'in_invoice':
                        qty += inv_line.product_uom_id._compute_quantity(inv_line.quantity, line.product_uom)
                    elif inv_line.move_id.move_type == 'in_refund':
                        qty -= inv_line.product_uom_id._compute_quantity(inv_line.quantity, line.product_uom)

            line.qty_invoiced = qty

            if line.order_id.state in ['purchase', 'done']:
                if line.is_down_payment:
                    line.qty_invoiced = line.product_qty
                if line.product_id.purchase_method == 'purchase':
                    line.qty_to_invoice = line.product_qty - line.qty_invoiced
                else:
                    line.qty_to_invoice = line.qty_received - line.qty_invoiced
            else:
                line.qty_to_invoice = 0