@api.onchange('branch_id', 'is_goods_orders', 'is_services_orders')
def _onchange_branch_update_approval_matrix(self):
    """Update approval matrix when branch or order type changes"""
    for record in self:
        if record.branch_id and record.is_blanket_order_approval_matrix:
            # First get the approval matrix
            matrix_id = False
            config = self.env['purchase.config.settings'].search([], limit=1, order="id desc")
            if config.is_blanket_order_approval_matrix:
                if record.is_goods_orders:
                    matrix_id = self.env['approval.matrix.blanket.order'].search(
                        [('branch_id', '=', record.branch_id.id), ('order_type', '=', 'goods_order')], limit=1)
                elif record.is_services_orders:
                    matrix_id = self.env['approval.matrix.blanket.order'].search(
                        [('branch_id', '=', record.branch_id.id), ('order_type', '=', 'services_order')], limit=1)
                else:
                    matrix_id = self.env['approval.matrix.blanket.order'].search(
                        [('branch_id', '=', record.branch_id.id), ('order_type_comb', '=', 'combined_order')], limit=1,
                        order='id desc')

                record.approval_matrix_id = matrix_id
                # Explicitly call the compute method to populate approved_matrix_ids
                if matrix_id:
                    record._compute_approving_matrix_lines_bo()