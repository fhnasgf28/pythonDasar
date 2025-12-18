from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

class Picking(models.Model):
    _inherit = 'stock.picking'

    def on_barcode_scanned(self, barcode):
        barcode_line = self.env['product.template.barcode'].search(
            [('name', '=', barcode)],
            limit=1
        )
        if not barcode_line:
            raise ValidationError(_("Scanned product is not found in the system."))

        product = barcode_line.product_id
        template = product.product_tmpl_id
        scanned_uom = barcode_line.uom_id
        if template.tracking != 'none':
            return
        move_lines = self.move_ids_without_package.filtered(
            lambda m: m.product_id == product
        )
        if not move_lines:
            raise ValidationError(
                _("Scanned product is not listed in the Operations line.")
            )
        move_line = move_lines[0]
        converted_qty = scanned_uom._compute_quantity(
            1,
            move_line.product_uom
        )
        move_line.quantity_done += converted_qty