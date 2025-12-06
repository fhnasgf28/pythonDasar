from odoo import models, fields, api

class ApprovalMatrixPurchaseRequest(models.Model):
    _inherit = 'purchase.request'

    @api.model
    def create(self, vals):
        config = self.env['purchase.config.settings'].search([], limit=1, order='id desc')
        if config and config.is_good_services_order:
            vals['order_type_comb'] = False
        else:
            vals['order_type'] = False
        return super(ApprovalMatrixPurchaseRequest, self).create(vals)

    def write(self, vals):
        config = self.env['purchase.config.settings'].search([], limit=1, order='id desc')
        if config and config.is_good_services_order:
            if 'order_type' in vals and 'order_type_comb' not in vals:
                vals['order_type_comb'] = False
        else:
            if 'order_type_comb' in vals and 'order_type' not in vals:
                vals['order_type'] = False
        return super(ApprovalMatrixPurchaseRequest, self).write(vals)

    def get_approval_matrix_request(self, type, department_id):
        domain = [('branch_id', '=', self.branch_id.id),
                  ('company_id', '=', self.company_id.id),
                  ('minimum_amt', '<=', self.amount_total),
                  ('maximum_amt', '>=', self.amount_total),
                  ('currency_id', '=', self.currency_id.id)]
        if type != 'combined_order':
            domain.append(('order_type', '=', type))
        else:
            domain.append(('order_type_comb', '=', type))
        if department_id:
            domain.append(('department_id', '=', department_id.id))

        # Debug: print domain and search results
        print("DEBUG - Approval Matrix Domain:", domain)
        print(
            "DEBUG - PR Values: branch_id=%s, company_id=%s, amount_total=%s, currency_id=%s, type=%s, department_id=%s" %
            (self.branch_id.id, self.company_id.id, self.amount_total, self.currency_id.id, type,
             department_id and department_id.id))

        # Check config setting
        config = self.env['purchase.config.settings'].search([], limit=1, order="id desc")
        is_good_services_order = config.is_good_services_order if config else False
        print("DEBUG - is_good_services_order config:", is_good_services_order)

        # Search with domain
        matrices = self.env['approval.matrix.purchase.request'].search(domain)
        print("DEBUG - Found matrices:", matrices.ids)
        if matrices:
            for matrix in matrices:
                print("DEBUG - Matrix %s: order_type=%s, order_type_comb=%s, min=%s, max=%s" %
                      (matrix.id, matrix.order_type, matrix.order_type_comb, matrix.minimum_amt, matrix.maximum_amt))

        approval_matrix_id = matrices[:1]
        return approval_matrix_id

    @api.depends('branch_id', 'company_id', 'department_id', 'currency_id', 'line_ids.product_qty',
                 'line_ids.estimated_cost')
    def _compute_approval_matrix_request(self):
        print("_compute_approval_matrix_request mantap bang")
        for record in self:
            record.approval_matrix_id = False
            if record.is_approval_matrix_request:
                print("DEBUG - is_approval_matrix_request:", record.is_approval_matrix_request)
                print("DEBUG - is_goods_orders:", record.is_goods_orders)
                print("DEBUG - is_services_orders:", record.is_services_orders)
                print("DEBUG - is_purchase_request_department:", record.is_purchase_request_department)

                if record.is_goods_orders and record.is_approval_matrix_request and record.is_purchase_request_department:
                    print("DEBUG - Path 1: goods_order with department")
                    approval_matrix_id = record.get_approval_matrix_request("goods_order", record.department_id)
                    record.approval_matrix_id = approval_matrix_id and approval_matrix_id.id or False
                elif record.is_services_orders and record.is_approval_matrix_request and record.is_purchase_request_department:
                    print("DEBUG - Path 2: services_order with department")
                    approval_matrix_id = record.get_approval_matrix_request("services_order", record.department_id)
                    record.approval_matrix_id = approval_matrix_id and approval_matrix_id.id or False
                elif record.is_goods_orders and record.is_approval_matrix_request:
                    print("DEBUG - Path 3: goods_order without department")
                    approval_matrix_id = record.get_approval_matrix_request("goods_order", False)
                    record.approval_matrix_id = approval_matrix_id and approval_matrix_id.id or False
                elif record.is_services_orders and record.is_approval_matrix_request:
                    print("DEBUG - Path 4: services_order without department")
                    approval_matrix_id = record.get_approval_matrix_request("services_order", False)
                    record.approval_matrix_id = approval_matrix_id and approval_matrix_id.id or False
                elif not record.is_goods_orders and record.is_approval_matrix_request:
                    print("DEBUG - Path 5: combined_order")
                    approval_matrix_id = record.get_approval_matrix_request("combined_order", False)
                    record.approval_matrix_id = approval_matrix_id and approval_matrix_id.id or False
                else:
                    print("DEBUG - Path 6: fallback")
                    if record.is_purchase_request_department:
                        approval_matrix_id = record.get_approval_matrix_request(False, record.department_id)
                        record.approval_matrix_id = approval_matrix_id and approval_matrix_id.id or False
                    else:
                        approval_matrix_id = record.get_approval_matrix_request(False, False)
                        record.approval_matrix_id = approval_matrix_id and approval_matrix_id.id or False
