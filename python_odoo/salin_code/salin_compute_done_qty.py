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
                    else:
                        pr_done_qty += line.qty_received
            if record.ir_lines_ids:
                for line in record.ir_lines_ids:
                    if line.transfer_qty and line.uom and record.product_unit_measure:
                        try:
                            converted_qty = line.uom._compute_quantity(line.transfer_qty, record.product_unit_measure)
                        except Exception:
                            converted_qty = line.transfer_qty
                        itr_done_qty += converted_qty
                    else:
                        itr_done_qty += line.transfer_qty or 0
            if record.itr_war_lines_ids:
                for line in record.itr_war_lines_ids:
                    itw_done_qty += line.quantity_done
            record.done_qty = pr_done_qty + itr_done_qty + itw_done_qty
            record.done_qty_dup = pr_done_qty + itr_done_qty
            record.done_qty_dup = 0
            record.requested_qty = record.quantity
            record.remaining_qty = abs(
                record.requested_qty - record.progress_quantity - record.done_qty)