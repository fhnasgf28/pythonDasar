from odoo import fields, models, api
from odoo.exceptions import ValidationError


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def on_barcode_scanned(self, barcode):
        print("Barcode scanned: %s", barcode)

        # 1. Cari barcode
        barcode_line = self.env['product.template.barcode'].search(
            [('name', '=', barcode)],
            limit=1
        )

        if not barcode_line:
            raise ValidationError(_("Scanned product is not found in the system."))

        # 2. Ambil product & template
        product = barcode_line.product_id  # product.product
        template = product.product_tmpl_id  # product.template
        scanned_uom = barcode_line.uom_id

        # 🔴 TRACKING CHECK (WAJIB & PALING AWAL)
        # Logic ini HANYA berlaku jika tracking = none
        if template.tracking != 'none':
            print(
                "Product %s has tracking %s, fallback to default behavior",
                product.display_name,
                template.tracking,
            )
            return super().on_barcode_scanned(barcode)

        # 3. Cari operation line
        move_lines = self.move_ids_without_package.filtered(
            lambda m: m.product_id == product
        )

        if not move_lines:
            raise ValidationError(
                _("Scanned product is not listed in the Operations line.")
            )

        move_line = move_lines[0]

        # 4. Convert UoM (1 scan = 1 unit barcode UoM)
        converted_qty = scanned_uom._compute_quantity(
            1,
            move_line.product_uom
        )

        # 5. Update done qty
        move_line.quantity_done += converted_qty