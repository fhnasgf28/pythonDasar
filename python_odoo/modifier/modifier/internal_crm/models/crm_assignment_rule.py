from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class CrmAssignmentRule(models.Model):
    _name = 'crm.assignment.rule'
    _description = 'CRM Assignment Rule'

    name = fields.Char(string='Rule Name', required=True)
    active = fields.Boolean(string='Active', default=True)
    rule_type = fields.Selection([
        ('round_robin', 'Round Robin'),
        ('by_location', 'By Location'),
        ('by_product', 'By Product Interest'),
        ('by_score', 'By Lead Score'),
        ('by_workload', 'By Workload'),
    ], string='Rule Type', required=True, default='round_robin')
    team_id = fields.Many2one('crm.team', string='Sales Team', help="Sales Team to which this rule applies")
    salesperson_ids = fields.Many2many(
        'res.users',
        string='Salespersons',
        domain="[('share', '=', False), ('sale_team_id', '=', team_id)]",
        help="Salespersons involved in this rule. Only non-portal users within the selected Sales Team will be available."
    )
    last_assigned_salesperson_id = fields.Many2one(
        'res.users',
        string='Last Assigned Salesperson',
        help="Used for Round Robin to track the last salesperson assigned."
    )
    location_field = fields.Char(string='Location Field', help="API name of the field containing location information (e.g., 'partner_id.city')")
    product_field = fields.Char(string='Product Interest Field', help="API name of the field containing product interest information")
    start_date = fields.Datetime(string="Start Date", required=True)
    end_date = fields.Datetime(string="End Date", required=True)
    display_name_with_date = fields.Char(
        string="Display Name with Date",
        compute="_compute_display_name_with_date"
    )

    def _compute_display_name_with_date(self):
        for record in self:
            start_date_str = record.start_date.strftime('%B %d, %Y %H:%M') if record.start_date else ''
            end_date_str = record.end_date.strftime('%B %d, %Y %H:%M') if record.end_date else ''
            record.display_name_with_date = f"{record.name} ({start_date_str} - {end_date_str})"

    @api.constrains('salesperson_ids')
    def _check_salesperson_team(self):
      for rule in self:
        if rule.salesperson_ids and rule.team_id:
          non_team_members = rule.salesperson_ids.filtered(lambda s: s.sale_team_id != rule.team_id)
          if non_team_members:
            raise ValidationError(_("Salespersons must be members of the selected Sales Team."))

    @api.onchange('team_id')
    def _onchange_team_id(self):
      self.salesperson_ids = [(5, 0, 0)]