from odoo import fields, models, api
from datetime import date

class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    stop_date = fields.Date(string='End Date', required=True)
    end_duration = fields.Date(string='End Duration', compute='_compute_end_duration', store=False, readonly=True)

    @api.depends('stop_date')  # Hanya perlu depends pada 'stop_date'
    def _compute_end_duration(self):
        for record in self:
            record.end_duration = record.stop_date  # Langsung salin nilai stop_date ke end_duration