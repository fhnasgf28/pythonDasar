from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import datetime, date


class BusinessAppointment(models.Model):
    _inherit = 'business.appointment'
    _description = 'Business Appointment'

    calendar_event_id = fields.Many2one('calendar.event', string='Calendar Event', readonly=True)


