from odoo import models, fields, api
from odoo.exceptions import ValidationError


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def close_purchase_order(self):
        for rec in self:
            if rec.is_services_orders:
                unmatched_lines = rec.order_line.filtered(
                    lambda line: line.actual_progress != (line.qty_invoiced / line.product_qty))
                if unmatched_lines:
                    raise ValidationError(
                        _("Purchase Order cannot be closed while actual progress is not the same as billed quantity.")
                        )
            else:
                product_data = defaultdict(lambda: {
                    'received': 0.0,
                    'invoiced': 0.0,
                    'has_bill': False  # Flag untuk melacak keberadaan bill
                })

                # Langkah 1: Agregasi data dari semua baris pesanan
                for line in rec.order_line:
                    if not line.product_id or line.display_type:
                        continue

                    product = line.product_id
                    product_data[product]['received'] += line.qty_received
                    product_data[product]['invoiced'] += line.qty_invoiced

                    # Cek apakah sudah ada bill (draft/posted) untuk produk ini.
                    # Jika sudah ketemu, tidak perlu cek lagi.
                    if not product_data[product]['has_bill']:
                        if line.invoice_lines.filtered(lambda inv: inv.move_id.state in ('draft', 'posted')):
                            product_data[product]['has_bill'] = True

                # Langkah 2: Validasi berdasarkan data yang sudah diagregasi
                problem_products_details = []
                for product, data in product_data.items():
                    # Cek apakah kuantitas tidak cocok
                    is_mismatched = fields.Float.compare(data['received'], data['invoiced'],
                                                         precision_rounding=product.uom_id.rounding) != 0

                    # Kondisi error: Kuantitas tidak cocok, DAN belum ada bill sama sekali, DAN sudah ada barang yang diterima.
                    if is_mismatched and not data['has_bill'] and data['received'] > 0:
                        problem_products_details.append(
                            _("- %s (Received: %s, Billed: %s, No Bill Found)") %
                            (product.display_name, data['received'], data['invoiced'])
                        )

                if problem_products_details:
                    error_details = "\n".join(problem_products_details)
                    raise ValidationError(
                        _("Purchase Order cannot be closed. The received quantity does not match the billed quantity and no bill has been created for the following products:\n\n%s") % error_details
                    )
                print(product_data)
                print(problem_products_details)
                print(product)