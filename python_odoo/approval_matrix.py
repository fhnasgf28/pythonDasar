@api.depends('amount', 'branch_id', 'currency_id')
    def _compute_approval_matrix_id(self):
        for record in self:
            set_approval_matrix = self.env['ir.config_parameter'].sudo().get_param('is_purchase_tender_approval_matrix')
            print('set_approval_matrix', set_approval_matrix)
            record.approval_matrix_id = False
            if record.is_approval_matrix and record.company_id and record.branch_id:
                approval_matrix_id = False
                if set_approval_matrix:
                    self.env.cr.execute("""
                            select id
                            from purchase_agreement_approval_matrix
                            where minimum_amt <= %s and
                            maximum_amt >= %s and
                            branch_id = %s and
                            company_id = %s and
                            currency_id = %s
                        """ % (record.amount, record.amount, record.branch_id.id, record.company_id.id,
                               record.currency_id.id))
                    approval_matrix_id = self.env.cr.fetchall()
                    approval_matrix_id = approval_matrix_id[0][0] if approval_matrix_id else False
                record.approval_matrix_id = approval_matrix_id