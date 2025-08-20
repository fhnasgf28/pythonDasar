def close_purchase_order(self):
    for rec in self:
        # --- Bagian 1: Validasi Utama (Sudah Benar) ---
        if rec.is_services_orders:
            unmatched_lines = rec.order_line.filtered(lambda line: line.actual_progress != line.qty_invoiced)
            error_msg = _("Purchase Order cannot be closed while actual progress is not the same as billed quantity.")
        else:
            unmatched_lines = rec.order_line.filtered(lambda line: line.qty_received != line.qty_invoiced)
            error_msg = _("Purchase Order can only be closed when the received amount is the same as the billed amount!")
        
        if unmatched_lines:
            raise ValidationError(error_msg)

        # --- Bagian 2: Validasi Pembayaran/DP ---
        # KOREKSI PENTING: Gunakan 'rec' bukan 'self' untuk memastikan konteks yang benar
        payment_invoice = rec.invoice_ids.filtered(lambda x: getattr(x, 'is_dp', False) and x.payment_state != 'not_paid')
        if payment_invoice:
            in_refund = sum(inv.amount_total for inv in payment_invoice if inv.move_type == 'in_refund')
            in_invoice = sum(inv.amount_total for inv in payment_invoice if inv.move_type == 'in_invoice')
            if in_refund != in_invoice:
                raise ValidationError(_("Purchase Order is unable to be closed while there’s an unrefunded advance payment bill. Please request the vendor to create a return bill."))

        # --- Bagian 3: Lakukan Aksi Terkait ---
        # BEST PRACTICE: Batalkan picking terlebih dahulu sebelum menutup PO
        for picking in rec.picking_ids.filtered(lambda x: x.state != 'done'):
            # Baris kode ini diasumsikan sudah benar dan berfungsi
            cancel_picking_id = self.env['cancel.picking'].create({
                'reason': "Purchase Order closed"
            })
            cancel_picking_id.with_context({'active_ids': picking.ids}).cancel_picking()

        # --- Bagian 4: Set Status Final ---
        # Panggil method ini sebagai langkah terakhir setelah semua validasi dan aksi berhasil
        rec.set_closed()
