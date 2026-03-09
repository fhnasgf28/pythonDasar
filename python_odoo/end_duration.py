from odoo import models, fields, api
from datetime import datetime, date

class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    description = fields.Text(string='Event Description')
    end_duration = fields.Float(string='End Duration (Hours)', compute='_compute_end_duration', store=False, readonly=False)

    @api.depends('stop_date', 'start_date')
    def _compute_end_duration(self):
        for record in self:
            if record.stop_date and record.start_date:
                record.end_duration = (record.stop_date - record.start_date).total_seconds() / 3600.0
            elif record.stop_date:
                today = date.today()
                duration = (record.stop_date - today).days
                record.end_duration = duration
            else:
                record.end_duration = 0.0
