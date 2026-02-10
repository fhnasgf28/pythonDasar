from odoo import models, exceptions, fields
from odoo.exceptions import ValidationError


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    cancel_reason = fields.Text('Cancel Reason')

    def action_purchase_cancel(self):
        for rec in self:
            for picking in rec.picking_ids:
                if picking.state == 'done':
                    raise ValidationError("You cannot cancel the purchase order that receiving notes already received")
            if rec.invoice_status != 'no':
                inv_not_cancel = self.invoice_ids.filtered(lambda p: p.state != 'cancel')
                if inv_not_cancel:
                    raise ValidationError("You need to cancel vendor bills before canceling the purchase order")
                else:
                    self.action_purchase_cancel()
            else:
                self.action_purchase_cancel()

    def action_purchase_cancel(self):
        for rec in self:
            if self._check_stock_installed():
                if rec.sudo().mapped('picking_ids').sudo().mapped('move_ids_without_package'):
                    rec.sudo().mapped('picking_ids').sudo().mapped(
                        'move_ids_without_package'
                    ).sudo().write({'state': 'cancel'})
                    rec.sudo().mapped('picking_ids').sudo().mapped('move_ids_without_package').mapped(
                        'move_line_ids'
                    ).sudo().write({'state': 'cancel'})
                rec._sh_unreserve_qty()
                rec.sudo().mapped('picking_ids').sudo().write(
                    {'state':'cancel'}
                )