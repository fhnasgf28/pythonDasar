from odoo import models, fields, api, _

class MaterialRequest(models.Model):
    _inherit = 'material.request.line'

    def _compute_itr_done_qty(self):
        for record in self:
            if record.ir_lines_ids:
                for line in record.ir_lines_ids:
                    record.itr_done_qty += line.transfer_qty
            else:
                record.itr_done_qty = 0

