from odoo import models, fields, api

class ApprovalMatrixPurchaseRequest(models.Model):
    _inherit = 'purchase.request'

    @api.model
    def create(self, vals):
        config = self.env['purchase.config.settings'].search([], limit=1, order='id desc')
        if config and config.is_good_services_order:
            vals['order_type_comb'] = False
        else:
            vals['order_type'] = False
        return super(ApprovalMatrixPurchaseRequest, self).create(vals)

    def write(self, vals):
        config = self.env['purchase.config.settings'].search([], limit=1, order='id desc')
        if config and config.is_good_services_order:
            if 'order_type' in vals and 'order_type_comb' not in vals:
                vals['order_type_comb'] = False
        else:
            if 'order_type_comb' in vals and 'order_type' not in vals:
                vals['order_type'] = False
        return super(ApprovalMatrixPurchaseRequest, self).write(vals)