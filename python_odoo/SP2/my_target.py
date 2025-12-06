from odoo import fields, models, api,_
from datetime import datetime

class MyTarget(models.Model):
    _name = 'my.target'
    _description = 'My Target'

    name = fields.Char(string='Name', required=True)
    target_amount = fields.Float(string='Target Amount', required=True)
    date = fields.Date(string='Date', required=True)

    @api.model
    def create(self, vals):
        vals['target_left'] = vals['main_target']
        # Handle both string and date objects
        start_date = vals['start_date']
        if isinstance(start_date, str):
            start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
        elif isinstance(start_date, datetime):
            start_date = start_date.date()

        end_date = vals['end_date']
        if isinstance(end_date, str):
            end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
        elif isinstance(end_date, datetime):
            end_date = end_date.date()

        my_target = self.env['crm.target'].search(
            [('salesperson_id', '=', self.env.user.id), ('state', '!=', 'rejected')])
        if my_target:
            for rec in my_target:
                rec.check_date(start_date, end_date)
        res = super().create(vals)
        res.name = self.env['ir.sequence'].next_by_code('crm.target.seq') or _('New')
        return res