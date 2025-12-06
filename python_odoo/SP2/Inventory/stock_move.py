from odoo import models, fields, api, _
from odoo.exceptions import UserError
import json


class StockMove(models.Model):
    _inherit = 'stock.move'

    width = fields.Float(string='Width', compute='_cal_move_width') 
    height = fields.Float(string='Height', compute='_cal_move_height')

    @api.depends('product_id', 'product_uom_qty', 'product_uom')
    def _cal_move_width(self):
        moves_with_width = self.filtered(lambda moves: moves.product_id.width > 0.00)
        for move in moves_with_width:   
            move.width = (move.product_qty * move.product_id.width)
        (self - moves_with_width).width = 0

    @api.depends('product_id', 'product_uom_qty', 'product_uom')
    def _cal_move_height(self):
        moves_with_height = self.filtered(lambda moves: moves.product_id.height > 0.00)
        for move in moves_with_height:
            move.height = (move.product_qty * move.product_id.height)
        (self - moves_with_height).height = 0

    def sh_stock_move_barcode_mobile_has_tracking(self, CODE_SOUND_SUCCESS, CODE_SOUND_FAIL):
        barcode = getattr(self, 'sh_stock_move_barcode_mobile', False)
        if barcode and self.picking_code == 'incoming' and self.product_id and self.product_id.tracking in ('lot', 'serial'):
            existing_lot = self.env['stock.production.lot'].search([
                ('name', '=', barcode),
                ('product_id', '=', self.product_id.id)
            ], limit=1)
            if existing_lot:
                raise UserError(_("Lot %s already exists") % barcode)

        return super(StockMove, self).sh_stock_move_barcode_mobile_has_tracking(CODE_SOUND_SUCCESS, CODE_SOUND_FAIL)

    @api.depends('ha_tracking', 'picking_type_id.use_create_lots', 'picking_type_id.use_existing_lots', 'state')
    def _compute_display_assign(self):
        for move in self:
            move.display_assign = (
                move.has_tracking in ('lot', 'serial') and
                move.state in ('partially_available', 'assigned', 'confirmed') and
                move.picking_type_id.use_create_lots and not move.picking_type_id.use_existing_lots
                and not move.origin_returned_move_id.id
            )

    @api.onchange('product_id')
    def _onchange_product_id_initial_uom(self):
        if self.product_id:
            self.initial_unit_of_measure = self.product_id.uom_id.id
            self.secondary_uom_id = self.product_id.secondary_uom_id.id

    def _compute_package_ids(self):
        for rec in self:
            packaging_ids = self.env['product.packaging'].search(
                [('product_id', 'in', self.product_id.ids)]
            )

    # @api.depends('location_id', 'product_id', 'move_id', 'move_id.origin_returned_move_id')
    # def _compute_lot_id_domain(self):
    #     for line in self:
    #         domain = [('id', '=', False)]
    #         move = self.env['stock.move'].browse(self.env.context.get('move_id'))
    #
    #         print(f"Computing lot domain for move: {move.id}")
    #
    #         if move.origin_returned_move_id:
    #             print(f"Move has origin_returned_move_id: {move.origin_returned_move_id.id}")
    #             # For return moves, get lots from original move lines
    #             lot_ids = move.origin_returned_move_id.move_line_ids.mapped('lot_id.id')
    #             print(f"Found lot_ids from origin move: {lot_ids}")
    #             if lot_ids:
    #                 domain = [('id', 'in', lot_ids)]
    #         else:
    #             # For normal moves, get lots with available quantity > 0 and not fully reserved
    #             if line.location_id and line.product_id:
    #                 # Get quants with available quantity
    #                 quants = self.env['stock.quant'].search([
    #                     ('location_id', '=', line.location_id.id),
    #                     ('product_id', '=', line.product_id.id),
    #                     ('lot_id', '!=', False),
    #                     ('quantity', '>', 0),
    #                     ('available_quantity', '>', 0)  # Only lots with available (non-reserved) quantity
    #                 ])
    #                 print("ini adalah quants", quants)
    #                 if quants:
    #                     lot_ids = quants.mapped('lot_id.id')
    #                     domain = [('id', 'in', lot_ids)]
    #                     print(f"Found available lots with quantity > 0: {lot_ids}")
    #                 else:
    #                     domain = [('id', '=', False)]  # No available lots
    #                     print("No available lots found with quantity > 0")
    #             else:
    #                 print("Location or product not set, using empty domain")
    #
    #         print(f"Final domain for move {move.id}: {domain}")
    #         line.lot_id_domain = json.dumps(domain)
    #

    @api.depends('location_id', 'product_id', 'move_id', 'move_id.origin_returned_move_id')
    def _compute_lot_id_domain(self):
        for line in self:
            domain = [('id', '=', False)]
            move = self.env['stock.move'].browse(self.env.context.get('move_id'))
            if move.origin_returned_move_id:
                lot_ids = move.origin_returned_move_id.move_line_ids.mapped('lot_id.id')
                if lot_ids:
                    domain = [('id', 'in', lot_ids)]
            else:
                if line.location_id and line.product_id:
                    all_quants = self.env['stock.quant'].search([
                        ('location_id', '=', line.location_id.id),
                        ('product_id', '=', line.product_id.id),
                        ('lot_id', '!=', False),
                    ])
                    available_quants = all_quants.filtered(lambda quant: quant.quantity > 0 and quant.available_quantity > 0 and (quant.quantity - quant.reserved_quantity) > 0)
                    if available_quants:
                        lot_ids = available_quants.mapped('lot_id.id')
                        domain = [('id', 'in', lot_ids)]
            line.lot_id_domain = json.dumps(domain)
