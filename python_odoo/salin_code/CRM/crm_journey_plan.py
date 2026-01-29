from odoo import api, fields, models, _
from odoo import tools
from datetime import datetime, timedelta
import json
from odoo.exceptions import UserError, ValidationError, Warning
import ssl
import certifi
import pytz
from geopy.geocoders import GoogleV3

class CrmJourneyPlan(models.Model):
    _name = 'crm.journey.plan'
    _description = 'CRM Journey Plan'
    _order = 'create_date desc'

    def _domain_salesperson_id(self):
        group = self.env.ref('equip3_crm_masterdata.group_team_member')
        return [('groups_id', 'in', group.ids), '|',('company_id', '=', self.env.company.id), ('company_id', '=', False)]

    @api.depends('calendar_ids')
    def _compute_meeting_count(self):
        for rec in self:
            rec.meeting_count = len(rec.calendar_ids)

    @api.depends('salesperson_id')
    def _compute_sale_team_(self):
        for rec in self:
            sale_team_id = False
            sale_team_leader_id = False
            if rec.salesperson_id:
                sale_team_ids = rec.salesperson_id.team_id or rec.salesperson_id.my_team_ids or rec.salesperson_id
                if sale_team_ids:
                    for team_id in sale_team_ids:
                        sale_team_id = team_id
                        break
                    sale_team_leader_id = sale_team_id.user_id
            rec.sale_team_id = sale_team_id
            rec.sale_team_leader_id = sale_team_leader_id

    @api.depends('plan_date')
    def _compute_day_name(self):
        for rec in self:
            if rec.plan_date:
                hari = rec.plan_date.strftime("%A")
                format_date = rec.plan_date.strftime("%d %B %Y")
                indonesian_date = f"{hari}, {format_date}"
                rec.day_name = indonesian_date
            else:
                rec.day_name = False


