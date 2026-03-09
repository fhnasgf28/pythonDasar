def _update_milestone_purchase_ids(self):
    """
    Metode internal untuk memperbarui milestone_purchase_ids berdasarkan milestone_template_id
    dan memastikan bahwa produk promo tidak ditambahkan ke SWO.
    """
    if self.milestone_template_id:
        # Mengisi milestone_purchase_ids berdasarkan milestone_template_id
        milestone_lines = self.milestone_template_id.mapped('milestone_line_ids')
        self.milestone_purchase_ids = [(5, 0, 0)]  # Hapus data lama
        self.milestone_purchase_ids = [(0, 0, {
            'name': line.name,
            'amount': line.amount,
        }) for line in milestone_lines]

        # Cari produk promo di purchase order
        promo_products = self.env['coupon.program'].search([]).mapped('discount_line_product_id')
        swo_records = self.env['service.work.order'].search([
            ('purchase_order_id', '=', self.id)
        ])

        for swo in swo_records:
            # Filter line yang merupakan produk promo
            promo_lines = swo.order_line.filtered(lambda line: line.product_id in promo_products)
            if promo_lines:
                # Hapus produk promo dari SWO
                promo_lines.unlink()


def write(self, vals):
    """
    Override metode write untuk menambahkan logika saat milestone_template_id diubah.
    """
    res = super(PurchaseOrder, self).write(vals)

    # Jika milestone_template_id diisi, panggil _update_milestone_purchase_ids
    if 'milestone_template_id' in vals:
        self._update_milestone_purchase_ids()

    return res
