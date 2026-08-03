from odoo import models, fields, api

class Repair(models.Model):
    _inherit = 'repair.order.model'

    @api.depends('invoice_ids')
    def _compute_invoice_count(self):
        for repair in self:
            repair.invoice_count = len(repair.invoice_ids)

    @api.depends('invoice_ids.state')
    def _compute_invoice_flags(self):
        for repair in self:
            draft_invoices = repair.invoice_ids.filtered(lambda inv: inv.state == 'draft')
            repair.has_draft_invoice = bool(draft_invoices)