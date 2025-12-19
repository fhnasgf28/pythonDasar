from odoo import models, fields, api, _

class PurchaseRequest(models.Model):
    _inherit = 'purchase.request'

    mr_id = fields.Many2many('material.request', 'pr_id','mr_id','pr_mr_id', string='Material Request')

    def button_done_pr(self):
        res = super(PurchaseRequest, self).button_done_pr()
        if self.mr_id:
            mr_rec = self.env['material.request'].search(
                [('id', 'in', self.mr_id.ids)]
            )
            for pr_line in self.line_ids:
                for mr_line in mr_rec.product_line:
                    if pr_line.product_id.id == mr_line.product.id:
                        for po in pr_line.purchase_lines:
                            mr_line.pr_in_progress_qty += po.product_qty
                            mr_line.pr_done_qty += po.qty_received

        return res

class PurchaseRequestLine(models.Model):
    _inherit = 'purchase.request.line'

    cancelled_qty = fields.Float(string='Cancelled Qty', default=0.0, readonly=True)
    mr_line_id = fields.Many2one('material.request.line', string='Material Request Line')

    @api.depends('purchase_lines.state', 'purchase_lines.move_ids.state', 'purchase_lines.move_ids.product_uom_qty')
    def _compute_qty(self):
        super(PurchaseRequestLine, self)._compute_qty()
        for line in self:
            if not line.purchase_request_allocation_ids:
                qty_in_progress = 0
                for po_line in line.purchase_lines:
                    moves = po_line.move_ids.filtered(lambda m:m.state not in ['done', 'cancel'])
                    for move in moves:
                        qty = move.product_uom_qty
                        if move.product_uom != line.product_uom_id:
                            qty = move.product_uom._compute_quantity(qty, line.product_uom_id)
                        qty_in_progress += qty
                    line.qty_in_progress = qty_in_progress


