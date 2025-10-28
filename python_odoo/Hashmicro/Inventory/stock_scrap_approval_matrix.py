from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class StockScrapLine(models.Model):
    _inherit = 'stock.scrap.line'

    @api.onchange('approver_types')
    def _onchange_approver_types(self):
        for data in self:
            if data.approver_types == 'by_hierarchy' and data.user_ids:
                data.user_ids = False

    def write(self, vals):
        res = super(StockScrapLine, self).write(vals)
        for data in self:
            if data.approver_types == 'by_hierarchy' and data.user_ids:
                data.user_ids = False
        return res

    @api.constrains('user_ids', 'minimum_approver')
    def check_approver_sequence(self):
        for record in self:
            if record.approver_types == 'by_hierarchy':
                if record.minimum_approver > len(record.user_ids):
                    raise ValidationError(_("Minimum Approver cannot be greater than the number of users."))

    @api.constrains('approver_types', 'sc_approval_matrix')
    def _check_single_by_hierarchy_per_matrix(self):
        for record in self:
            if record.approver_types == 'by_hierarchy' and record.sc_approval_matrix:
                siblings = record.sc_approval_matrix.sc_approval_matrix_line_ids
                others = siblings.filtered(lambda x: x.id != record.id and x.approver_types == 'by_hierarchy')
                if others:
                    raise ValidationError(_("Only one scrap line can have 'By Hierarchy' approver type per matrix."))
