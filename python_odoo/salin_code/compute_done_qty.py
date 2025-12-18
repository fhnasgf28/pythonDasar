from odoo import fields,models, api, _

class MaterialRequestLine(models.Model):
    _inherit = 'material.request.line'

    def _compute_done_qty(self):
        for record in self:
            pr_done_qty = 0
            itr_done_qty = 0
            itw_done_qty = 0
            if record.pr_lines_ids:
                for line in record.pr_lines_ids:
                    if line.product_uom_id != record.product_unit_measure:
                        pr_done_qty += line.product_uom_id._compute_quantity(line.qty_received, record.product_unit_measure)
                        print("ini adalah pr done qty bagian if", pr_done_qty)
                    else:
                        pr_done_qty += line.qty_received
                        print("ini adalah pr done qty bagian else", pr_done_qty)
            if record.ir_lines_ids:
                for line in record.ir_lines_ids:
                    if line.uom and record.product_unit_measure and line.uom != record.product_unit_measure:
                        itr_done_qty += line.uom._compute_quantity(line.transfer_qty, record.product_unit_measure)
                        print("ini adalah itr done qty bagian if", itr_done_qty)
                    else:
                        itr_done_qty += line.transfer_qty or 0
                        print("ini adalah itr done qty bagian else", itr_done_qty)

            if record.itr_war_lines_ids:
                for line in record.itr_war_lines_ids:
                    if line.product_uom and record.product_unit_measure and line.product_uom != record.product_unit_measure:
                        itw_done_qty += line.product_uom._compute_quantity(line.quantity_done, record.product_unit_measure)
                        print("ini adalah itw done qty bagian if", itw_done_qty)
                    else:
                        itw_done_qty += line.quantity_done
                        print("ini adalah itw done qty bagian else")
            record.done_qty = pr_done_qty + itr_done_qty + itw_done_qty
            record.done_qty_dup = pr_done_qty + itr_done_qty
            record.done_qty_dup = 0
            record.requested_qty = record.quantity
            record.remaining_qty = abs(
                record.requested_qty - record.progress_quantity - record.done_qty)