from odoo import fields, models, api
from datetime import datetime
import pytz

class PurchaseRequisition(models.Model):
    _inherit = 'purchase.requisition'

    def _get_default_date_end(self, date_value=None):
        user = self.env.user
        tz = pytz.timezone(user.tz or 'UTC')
        if not date_value:
            target_date = datetime.now(tz).date()
        elif isinstance(date_value, datetime):
            target_date = date_value.date()
        else:
            target_date = date_value
        noon_local = datetime.combine(target_date, datetime.min.time().replace(hour=12))
        noon_local_tz = tz.localize(noon_local)
        noon_utc = noon_local_tz.astimezone(pytz.UTC)
        noon_naive = noon_utc.replace(tzinfo=None)
        return noon_naive