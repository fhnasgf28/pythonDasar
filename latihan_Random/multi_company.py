from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class res_partner(models.Model):
    @api.model
    def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
        print('search_read')
        domain = domain or []
        domain = self._get_company_domain() + self._get_branch_domain() + domain
        print("mantap banget nih bnag", domain)
        return super().search_read(domain=domain, fields=fields, offset=offset, limit=limit, order=order)


    def _get_company_domain(self):
        domain = []
        allowed_companies = self.env.context.get('allowed_company_ids')
        if allowed_companies:
            if len(self.env.companies) == 1:
                domain += ['|', ('company_id', '=', self.env.company.id), ('company_id', '=', False)]
            else:
                domain += ['|', ('company_id', 'in', self.env.companies.ids), ('company_id', '=', False)]
        return domain


    def _get_branch_domain(self):
        domain = []
        if self.env.branches:
            domain += ['|', ('branch_id', 'in', self.env.branches.ids), ('branch_id', '=', False)]
        return domain

    @api.depends('branch_id', 'sh_agreement_type', 'amount')
    def _get_approval_matrix(self):
        set_approval_matrix = self.env['ir.config_parameter'].sudo().get_param('is_purchase_tender_approval_matrix')
        config = self.env['purchase.config.settings'].search([], limit=1, order="id desc")
        context = dict(self._context or {})
        is_good_services_order = config.is_good_services_order
        for res in self:
            res.approval_matrix = False
            if set_approval_matrix:
                approval_id = False
                if is_good_services_order and context.get('default_is_goods_orders'):
                    approval_id = self.env['purchase.agreement.approval.matrix'].search([('branch_id', '=', res.branch_id.id), ('order_type', '=', 'goods_order')], limit=1, order='id desc')
                elif is_good_services_order and context.get('default_is_services_orders'):
                    approval_id = self.env['purchase.agreement.approval.matrix'].search([('branch_id', '=', res.branch_id.id), ('order_type', '=', 'services_order')], limit=1, order='id desc')
                else:
                    approval_id = self.env['purchase.agreement.approval.matrix'].search([('branch_id', '=', res.branch_id.id)], limit=1, order='id desc')
                res.approval_matrix = approval_id

    @api.depends('state', 'salesperson_id', 'team_leader_id')
    def _compute_hide(self):
        for rec in self:
            hide = False
            if rec.state == 'draft' and not rec.sale_team_id.member_ids:
                hide = True
            if rec.state == 'waiting_approval':
                if self.env.user.id != rec.team_leader_id.id:
                    if self.env.user.id not in rec.sale_team_id.additional_leader_ids.ids:
                        hide = True
            if rec.state == 'rejected':
                if self.env.user.id != rec.salesperson_id.id and self.env.user.id != rec.team_leader_id.id and self.env.user.id not in rec.sale_team_id.additional_leader_ids.ids:
                    hide = True
            rec.hide = hide