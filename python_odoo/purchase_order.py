def action_apply(self):
    for record in self:
        record.order_line.write({'destination_warehouse_id': record.destination_warehouse_id})


def _compute_approval_matrix(self):
    IrConfigParam = self.env['ir.config_parameter'].sudo()
    approval = IrConfigParam.get_param('is_purchase_order_approval_matrix')
    # approval = self.env.company.is_purchase_order_approval_matrix
    for record in self:
        record.is_approval_matrix = approval


def _get_approve_button(self):
    for record in self:
        matrix_line = sorted(record.approved_matrix_ids.filtered(lambda r: not r.approved), key=lambda r: r.sequence)
        if len(matrix_line) == 0:
            record.is_approve_button = False
            record.approval_matrix_line_id = False
        elif len(matrix_line) > 0:
            matrix_line_id = matrix_line[0]
            if self.env.user.id in matrix_line_id.user_ids.ids and self.env.user.id != matrix_line_id.last_approved.id:
                record.is_approve_button = True
                record.approval_matrix_line_id = matrix_line_id.id
            else:
                record.is_approve_button = False
                record.approval_matrix_line_id = False
        else:
            record.is_approve_button = False
            record.approval_matrix_line_id = False