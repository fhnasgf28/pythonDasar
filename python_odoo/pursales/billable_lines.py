def change_price_dp(self):
    self.env.context = dict(self._context)
    print("beuuhh woke mamang")
    for rec in self:
        for inv_line in rec.invoice_line_ids:
            if rec.purchase_order_ids:
                dp_lines = self.env['purchase.down.payment'].search([
                    ('purchase_id', 'in', rec.purchase_order_ids.ids),
                    ('is_down_payment_by_billable', '=', True)
                ])
                print("ini adalah dp lines")
                if not dp_lines:
                    print("ini adalah mantap", not dp_lines)
                    self.env.context.update({'cancel': False})
                for line in inv_line.purchase_line_id:
                    line.price_unit = 0 if self.env.context.get('cancel') else inv_line.price_unit
                    print("ini adalah mantap", line.price_unit)
            if rec.sale_order_ids:
                if not rec.is_dp:
                    self.env.context.update({'cancel': False})
                for line in inv_line.sale_line_ids:
                    line.price_unit = 0 if self.env.context.get('cancel') else inv_line.price_unit