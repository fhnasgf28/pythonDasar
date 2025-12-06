from odoo import models, fields, api
from datetime import datetime

class NewReceiptId(models.Model):
    _inherit = 'stock.picking'

    def _compute_new_receipt_id(self):
        new_receipt_id = False
        for line in self.rma_lines:
            if line.action == 'replace_same':
                purchase_price = 0.0
                if self.purchase_id:
                    po_line = self.purchase_id.order_line.filtered(lambda l: l.product_id.id == line.product_id.id)[:1]
                    if po_line:
                        purchase_price = po_line.price_unit
                    if not purchase_price and line.picking_id:
                        move = line.picking_id.move_ids_without_package.filtered(lambda m: m.product_id.id == line.product_id.id and m.purchase_line_id)[:1]
                        if move and move.purchase_line_id:
                            purchase_price = move.purchase_line_id.price_unit
                    if not new_receipt_id:
                        picking_vals = {
                            'partner_id' : self.partner_id.id,
                            'picking_type_id': self.warehouse_id.in_type_id.id,
                            'company_id': self.company_id.id,
                            'user_id': self.create_uid.id,
                            'date': datetime.now(),
                            'origin': self.name,
                            'location_dest_id': self.location_id if self.location_id else self.warehouse_id.lot_stock_id.id,
                            'location_id': self.warehouse_id.lot_stock_id.id,
                            'branch_id': self.branch_id.id,
                            'rma_id': self.id,
                        }
                        new_receipt_id = self.env['stock.picking'].create(picking_vals)

                    move_vals = {
                        'product_id': line.product_id.id,
                        'name': line.product_id.name,
                        'product_uom_qty': line.return_qty,
                        'product_uom':line.product_id.uom_id.id if line.product_id.uom_id else False,
                        'price_unit': purchase_price,
                        'picking_id': new_receipt_id,
                        'date': datetime.now(),
                        'state': 'draft',
                        'origin': self.name,
                        'warehouse_id': self.warehouse_id.id,
                        'location_id': self.warehouse_id._get_partner_locations()[1].id,
                        'location_dest_id': self.location_id.id or self.warehouse_id.lot_stock_id.id,
                    }

                    new_move = self.env['stock.move'].create(move_vals)
                    line.replace_move_id = new_move.id
        if new_receipt_id:
            new_receipt_id.action_confirm()