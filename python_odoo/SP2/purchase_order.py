from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT

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

    def _compute_hold_purchase_order(self):
        for record in self:
            if self.env.user.has_group('equip3_purchase_operation.group_purchase_order_partner_credit_limit'):
                record.is_hold_purchase_order = True
            else:
                record.is_hold_purchase_order = False

    def button_on_hold_confirm(self):
        self.state = 'sent'
        self.with_context(order_confirm=True).button_confirm()


    @api.onchange('partner_id', 'company_id')
    def onchange_partner_id(self):
        res = super(PurchaseOrder,self).onchange_partner_id()
        self._compute_hold_purchase_order()
        return res

    def check_expected_date(self):
        params = {'order_id':self.id}
        for rec in self.order_line.filtered(lambda x:not x.display_type):
            seller = rec.product_id._select_seller_expected_date(
                partner_id = rec.partner_id,
                quantity=rec.product_qty,
                date=datetime.now(),
                uom_id=rec.product_uom,
                params=params
            )
            planned_date = rec._get_date_planed(seller) if seller else datetime.now()
            planned_date = planned_date.date()
            planned_datetime = datetime.now().replace(year=planned_date.year, month=planned_date.month, day=planned_date.day)
            rec.date_planed = planned_datetime.strftime(DEFAULT_SERVER_DATE_FORMAT)
