from odoo import models, fields, api


class StockMove(models.Model):
    _inherit = 'stock.move'

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