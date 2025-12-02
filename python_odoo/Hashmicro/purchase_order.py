from odoo import models, fields, api
from odoo.exceptions import ValidationError

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.model
    def create(self, vals):
        res = super(PurchaseOrder, self).create(vals)
        return res

    @api.model
    def _default_domain(self):
        context = dict(self.env.context) or {}
        domain = [('company_id', '=', self.env.company.id), ('purchase_ok', '=', True)]
        if context.get('goods_order'):
            return domain+[('type', 'in', ('consu', 'product'))]
        elif context.get('service_order'):
            return domain+[('type', '=', 'service')]
        return domain

    @api.onchange('dest_loc_id')
    def _compute_picking_type(self):
        for res in self:
            if res.dest_loc_id:
                if res.picking_type_id:
                    res.picking_type_dest = res.dest_loc_id.picking_type_id
                else:
                    raise ValidationError("Picking Type not found")

    def action_reject(self):
        if self.state != 'waiting_for_approve':
            return {
                'type': 'ir.actions.client',
                'tag': 'reload',
            }
        return {
            'type': 'ir.actions.act_window',
            'name': 'rejected reason',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'approval.reject',
            'target': 'new'
        }