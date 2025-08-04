from odoo import api, fields, models
from odoo.exceptions import ValidationError

class CrmTarget(models.Model):
    _inherit = 'crm.target'
    def check_date(self, start_date, end_date, based_on):
        for rec in self:
            overlapping_targets = self.env['crm.target'].search([
                ('id', '!=', rec.id),
                ('salesperson_id', '=', rec.salesperson_id.id),
                ('based_on', '=', based_on),
                ('state', '!=', 'rejected'),
                '|', '|',
                '&', ('start_date', '<=', start_date), ('end_date', '>=', start_date),
                '&', ('start_date', '<=', end_date), ('end_date', '>=', end_date),
                '&', ('start_date', '>=', start_date), ('end_date', '<=', end_date),
            ])

            if overlapping_targets:
                raise ValidationError(
                    f"There is already existing target data overlapping this date range "
                    f"with the same basis '{based_on.replace('_', ' ').title()}'. "
                )