from odoo import models, api
class CrmJourneyPlanLine(models.Model):
    _inherit = 'crm.journey.plan.line'

    # Override the search method to filter by company_id
    # This ensures that only records belonging to the current company are returned
    # This is useful in a multi-company environment to prevent data leakage between companies.

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        # Menambahkan filter untuk company_id
        company_id = self.env.company.id
        new_args = list(args)
        new_args.append(('company_id', '=', company_id))
        return super(CrmJourneyPlanLine, self).search(new_args, offset=offset, limit=limit, order=order, count=count)
        # berikan keterangan bahwa kita menambahkan filter company_id
        # untuk memastikan hanya data yang sesuai dengan perusahaan saat ini yang dikembalikan.
        # Ini berguna dalam lingkungan multi-perusahaan untuk mencegah kebocoran data antar perusahaan.