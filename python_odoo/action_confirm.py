from odoo import models, fields, api
import logging
class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.depends('approving_matrix_sale_id','is_over_limit_validation','state','approval_matrix_state')
    def _compute_show_action_confirm(self):
        _logger = logging.getLogger(__name__)
        for rec in self:
            show_action_confirm = True
            if rec.is_over_limit:
                if rec.state != 'quotation_approved':
                    show_action_confirm = False
            if rec.is_customer_approval_matrix:
                if rec.state != 'quotation_approved':
                    show_action_confirm = False
                    print("DEBUG - Button hidden because is_customer_approval_matrix=True and state != quotation_approved")
            if not rec.is_over_limit and not rec.is_customer_approval_matrix:
                if rec.state not in ('draft','sent'):
                    show_action_confirm = False
                    print("DEBUG - Button hidden because state not in ('draft', 'sent')")
            # Pastikan tombol confirm selalu muncul ketika state adalah 'sent'
            if rec.state == 'sent':
                show_action_confirm = True
                print("DEBUG - Forcing button to show because state is 'sent'")
                
            rec.show_action_confirm = show_action_confirm
            print("DEBUG - Final show_action_confirm value revisi: %s", show_action_confirm)