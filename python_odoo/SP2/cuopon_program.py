from odoo import models, fields, api
import json


class CouponProgram(models.Model):
    _inherit = 'coupon.program'

    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        res['sale_discount_line_product_id_domain'] = json.dumps(
            ['|', ('company_ids', '=', False), ('company_ids', 'in', self.env.company.id), ('type', '=', 'service')])
        res['sale_reward_product_id_domain'] = json.dumps(
            ['|', ('company_ids', '=', False), ('company_ids', 'in', self.env.company.id)])
        return res

    def search_read(self, domain=None, fields=None, offset=0, limit=None, order=None):
        if self.env.context.get('allowed_company_ids'):
            company_ids = self.env.companies.ids
            branch_ids = self.env.branches.ids

            branch_domain = ['|', ('branch_id', 'in', branch_ids), ('branch_id', '=', False)]
            domain = (domain or []) + [('company_id', 'in', company_ids)] + branch_domain
