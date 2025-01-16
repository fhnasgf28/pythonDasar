from odoo import models, fields, api
from datetime import datetime, date
from odoo.exceptions import UserError, ValidationError


class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    description = fields.Text(string='Event Description')
    end_duration = fields.Char(string='End Duration', compute='_compute_end_duration', store=True, readonly=True)
    business_appointment_id = fields.Many2one('business.appointment', string='Business Appointment', readonly=True)
    resource_type_id = fields.Many2one('business.resource.type', string='Resource Type')
    service_id = fields.Many2one('appointment.product', string='Service')
    resource_id = fields.Many2one('business.resource', string='Resources')

    @api.model
    def create(self, vals_list):
        print('farhanassegaf apakah kodingan ini akan kamu eksekusi')
        events = super(CalendarEvent, self).create(vals_list)
        for event, vals in zip(events, vals_list):
            if not event.business_appointment_id:
                partner = event.partner_id.id if event.partner_id else False
                appointment_vals = {
                    'name': event.name,
                    'datetime_start': event.start_date,
                    'datetime_end': event.stop_date,
                    'calendar_event_id': event.id,
                    'partner_id': partner,
                    'resource_id': event.resource_id.id,
                    'resource_type_id': event.resource_type_id.id,
                    'service_id': event.service_id.id,
                }
                appointment = self.env['business.appointment'].create(appointment_vals)
                event.business_appointment_id = appointment.id
        return events

    @api.constrains('stop_date', 'start_date','resource_id')
    def _check_dates(self):
        for event in self:
            if event.start_date and event.stop_date and event.resource_id:
                for resource in event.resource_id:
                    if self.env['business.appointment'].check_overlap(
                            event.start_date,
                            event.stop_date,
                            event.resource_id.id,
                            event.business_appointment_id.id if event.business_appointment_id else None):
                        raise ValidationError(f"Konflik jadwal terdeteksi di Business Appointment untuk resource: {resource.name} pada waktu yang sama!")

    def check_overlap(self, start_datetime, stop_datetime, exclude_id=None):
        """
        Checks for overlapping appointments.

        :param start_datetime: The start datetime of the appointment.
        :param stop_datetime: The stop datetime of the appointment.
        :param exclude_id: Optional ID of the appointment to exclude from the check.
        :return: True if there is an overlap, False otherwise.
        """
        domain = [
            ('start_datetime', '<', stop_datetime),
            ('stop_datetime', '>', start_datetime),
        ]
        if exclude_id:
            domain.append(('id', '!=', exclude_id))
        return self.search_count(domain) > 0

    @api.depends('stop_date')
    def _compute_end_duration(self):
        for record in self:
            if record.stop_date:
                record.end_duration = record.stop_date.strftime("%B %d, %Y")
            else:
                record.end_duration = False
