from odoo import api, models

class ActivityReportInherit(models.Model):
    _inherit = 'crm.activity.report'

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        if self.env.context.get('allowed_company_ids'):
            if len(self.env.companies) == 1:
                args += [('company_id', 'in', self.env.companies.ids)]
            else:
                args += [('company_id', 'in', self.env.context['allowed_company_ids'])]

        return super(ActivityReportInherit, self).search(args, offset=offset, limit=limit, order=order, count=count)