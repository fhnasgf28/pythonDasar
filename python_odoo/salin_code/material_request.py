from odoo import fields, models, api

class materialRequest(models.Model):
    _inherit = 'material.request'

    def update_progress_quantity_on_po_confirm(self, po_lines):
        """
        Update In Progress Quantity pada MR Line setelah PO dikonfirmasi
        Args:
            po_lines: recordset of purchase.order.line yang dikonfirmasi
        """
        for po_line in po_lines:
            # Cari PR line yang terkait dengan PO line ini
            pr_lines = self.env['purchase.request.line'].search([
                ('purchase_lines', 'in', po_line.ids)
            ])

            for pr_line in pr_lines:
                if pr_line.mr_line_id:
                    # Trigger recompute progress_quantity
                    pr_line.mr_line_id._compute_progress_quantity()

    def update_progress_quantity_on_po_cancel(self, po_lines):
        """
        Update In Progress Quantity pada MR Line setelah PO dibatalkan
        Args:
            po_lines: recordset of purchase.order.line yang dibatalkan
        """
        for po_line in po_lines:
            # Cari PR line yang terkait dengan PO line ini
            pr_lines = self.env['purchase.request.line'].search([
                ('purchase_lines', 'in', po_line.ids)
            ])

            for pr_line in pr_lines:
                if pr_line.mr_line_id:
                    # Trigger recompute progress_quantity
                    pr_line.mr_line_id._compute_progress_quantity()

    def update_progress_quantity_on_rn_confirm(self, stock_pickings):
        """
        Update In Progress Quantity pada MR Line setelah RN dikonfirmasi
        Args:
            stock_pickings: recordset of stock.picking (RN) yang dikonfirmasi
        """
        for picking in stock_pickings:
            if picking.picking_type_code == 'incoming' and picking.purchase_id:
                # Update progress quantity untuk semua MR lines yang terkait
                for move in picking.move_lines:
                    pr_lines = self.env['purchase.request.line'].search([
                        ('purchase_lines.move_ids', 'in', move.ids)
                    ])

                    for pr_line in pr_lines:
                        if pr_line.mr_line_id:
                            # Trigger recompute progress_quantity
                            pr_line.mr_line_id._compute_progress_quantity()

    def update_progress_quantity_on_rn_cancel(self, stock_pickings):
        """
        Update In Progress Quantity pada MR Line setelah RN dibatalkan
        Args:
            stock_pickings: recordset of stock.picking (RN) yang dibatalkan
        """
        for picking in stock_pickings:
            if picking.picking_type_code == 'incoming' and picking.purchase_id:
                # Update progress quantity untuk semua MR lines yang terkait
                for move in picking.move_lines:
                    pr_lines = self.env['purchase.request.line'].search([
                        ('purchase_lines.move_ids', 'in', move.ids)
                    ])

                    for pr_line in pr_lines:
                        if pr_line.mr_line_id:
                            # Trigger recompute progress_quantity
                            pr_line.mr_line_id._compute_progress_quantity()