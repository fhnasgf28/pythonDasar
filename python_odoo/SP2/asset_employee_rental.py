from odoo import models, fields, api, _
from odoo.tools import relativedelta

class AssetEmployeeRental(models.Model):
    _name = 'asset.employee.rental'
    _description = 'Asset Employee Rental'

    def create_rental_returns(self):
        for rec in self:
            today = fields.Date.today()
            due_date = rec.date_to.date() if rec.date_to else today
            if not due_date or due_date <= today:
                due_date = today + relativedelta(days=1)

            ret = self.env['employee.asset.return'].create({
                'rental_reference': rec.id,
                'due_date': due_date,
                'branch_id': rec.branch_id.id or False,
                'description':_('Return for %') % rec.name,
                'assets_line': [
                    (0,0, {
                        'asset_id': rec.asset_id.id,
                        'employee_id': line.asset_id.pic_id.id if line.asset_id and line.asset_id.pic_id else False,
                        'notes': line.notes,
                    })
                    for line in rec.rental_line if line.asset_id
                ]
            })

            return {
                'type': 'ir.actions.act_window',
                'res_model': 'employee.asset.return',
                'res_id': ret.id,
                'view_mode': 'form',
                'target': 'new',
                'context': {'default_rental_reference': rec.id},
            }

    def _compute_return_count(self):
        for rec in self:
            rec.return_count = self.env['employee.asset.return'].search_count([('rental_reference', '=', rec.id)])