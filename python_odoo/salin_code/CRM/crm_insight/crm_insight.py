import datetime
import calendar
import pandas as pd
from odoo import models, fields, api
from odoo.tools import date_utils
from odoo.http import request
from datetime import datetime, date, timedelta
import logging
_logger = logging.getLogger(__name__)

class CRMLead(models.Model):
    _inherit = 'crm.lead'
    _description = 'CRM Lead'

    crm_manager_id = fields.Many2one('res.users', string='CRM Manager', strore=True)
    monthly_goal = fields.Float(string="Monthly Goal")
    achievement_amoun = fields.Float(string="Monthly Achievement")

    @api.model
    def _get_currency(self):
        currency_array = [self.env.user.company_id.currency_id.id.symbol, self.env.user.company_id.currency_id.id.name]
        return currency_array

    @api.model
    def check_user_group(self):
        user = self.env.user
        if user.has_group('sales_team.group_sale_manager'):
            return True
        else:
            return False

    def get_last_month(self):
        today = fields.Date.today()
        first = today.replace(day=1)
        last_month = first + timedelta(days=-1)
        return last_month

    def get_last_quarter(self):
        today = fields.Date.today()
        up2date = fields.Date.today()
        quarter = pd.Timestamp(today).quarter
        for i in range(4):
            last_day_of_prev_month = up2date.replace(day=1)
            quarter2 = pd.Timestamp(last_day_of_prev_month).quarter
            if quarter2 == (quarter - 1):
                break
            up2date = last_day_of_prev_month
        last_quarter = last_day_of_prev_month
        return last_quarter

