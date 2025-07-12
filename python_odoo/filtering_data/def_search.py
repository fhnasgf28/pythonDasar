from odoo import models, api
class CrmJourneyPlanLine(models.Model):
    _inherit = 'crm.journey.plan.line'

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        # Add filter for company_id to ensure only records belonging to the current company are returned
        company_ids = self.env.companies.id
        new_args = list(args)
        if len (company_ids) > 1:
            new_args.append(('company_id', 'in', company_ids))
        else:
            new_args.append(('company_id', '=', self.env.company.id))
        return super(CrmJourneyPlanLine, self).search(new_args, offset=offset, limit=limit, order=order, count=count)