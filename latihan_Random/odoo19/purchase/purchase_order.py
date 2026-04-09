from odoo import api, fields, models, _
from datetime import datetime

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.depends('order_line.invoice_lines.move_id')
    def _compute_invoice(self):
        for order in self:
            invoices = order.mapped('order_line.invoice_lines.move_id')
            order.invoice_ids = invoices
            order.invoice_count = len(invoices)

    @api.depends('state', 'date_order','date_approve')
    def _compute_date_calendar_start(self):
        for order in self:
            order.date_calendar_start = order.date_approve if (order.state == 'purchase') else order.date_order

    def _compute_access_url(self):
        super(PurchaseOrder, self)._compute_access_url()
        for order in self:
            order.access_url = 'my/purchase/%s' % (order.id)

    @api.depends('order_line.date_planned')
    def _compute_date_planned(self):
        for order in self:
            dates_list = order.order_line.filtered(lambda x: not x.display_type and x.date_planned).mapped('date_planned')
            if dates_list:
                order.date_planned = max(dates_list)
            else:
                order.date_planned = False

    @api.depends('partner_ref', 'origin', 'partner_id')
    def _compute_duplicated_order_ids(self):
        draft_orders = self.filtered(lambda o: o.state == 'draft')
        order_to_duplicate_orders = draft_orders._fetch_duplicate_orders()
        for order in draft_orders:
            duplicate_ids = order_to_duplicate_orders.get(order.id, [])
            order.duplicated_order_ids = [(6, 0, duplicate_ids)]
        (self - draft_orders).duplicated_order_ids = False

    def action_open_business_doc(self):
        self.ensure_one()
        return {
            'name': _('Business Doc uments'),
            'type': 'ir.actions.act_url',
            'target': 'new',
            'views': [(False, 'form')]
        }

    def print_quotation(self):
        self.filtered(lambda po: po.state == 'draft').write({'state': "sent"})
        return self.env.ref('purchase.report_purchase_quotation').report_action(self)

    def button_approve(self, force=False):
        self = self.filtered(lambda order: order._approval_allowed())
        self.write({'state': 'purchase', 'date_approve': fields.Datetime.now()})
        self.filtered(lambda p: p.lock_confirmed_po == 'lock').write({'locked': True})