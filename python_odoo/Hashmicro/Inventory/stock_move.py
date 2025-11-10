from odoo import models, fields, api, _
from odoo.exceptions import UserError


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


