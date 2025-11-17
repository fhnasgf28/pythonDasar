from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def _create_picking(self):
        res = super(PurchaseOrder, self)._create_picking()
        context = dict(self.env.context) or {}
        if context.get('is_product_service_operation_receiving'):
            self._create_picking_service()
        return res

    def _prepare_picking(self):
        res = super(PurchaseOrder, self)._prepare_picking()
        rn_approval_matrix_config = self.env['inventory.config.settings'].search([('is_receiving_notes_approval_matrix', '=', True)])
        res.update({
            'is_receiving_notes_approval_matrix': rn_approval_matrix_config.is_receiving_notes_approval_matrix,
            'approval_matrix_receiving_id': rn_approval_matrix_config.approval_matrix_receiving_id,
        })
        return res

    def button_onhold_confirm(self):
        self.state = 'sent'
        self.with_context(order_confirm=True).button_confirm()

    def onchange_partner_id(self):
        res = super(PurchaseOrder, self).onchange_partner_id()
        self._compute_hold_purchase_order()
        return res

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'


