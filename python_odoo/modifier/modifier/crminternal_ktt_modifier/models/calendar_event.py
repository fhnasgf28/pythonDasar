from odoo import models, fields, api
from datetime import datetime, date, timedelta
from odoo.exceptions import UserError, ValidationError


class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    description = fields.Text(string='Event Description')
    end_duration = fields.Char(string='End Duration', compute='_compute_end_duration', store=True, readonly=True)
    business_appointment_id = fields.Many2one('business.appointment', string='Business Appointment', readonly=True)
    resource_type_id = fields.Many2one('business.resource.type', string='Resource Type', required=True)
    service_id = fields.Many2one('appointment.product', string='Service', required=True)
    resource_id = fields.Many2one('business.resource', string='Resources', required=True)
    lead_id = fields.Many2one('crm.lead', string='Lead')
    in_this_week = fields.Boolean(string="In This Week", default=False, store=False)

    def _cron_update_meeting_status(self):
        today = date.today()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        # Convert date objects to datetime objects
        start_of_week_dt = datetime.combine(start_of_week, datetime.min.time())
        end_of_week_dt = datetime.combine(end_of_week, datetime.max.time())
        # 1. Find events this week and in_this_week is not True
        calendar_event = self.env['calendar.event']
        events_this_week = calendar_event.search([
            ('start', '>=', start_of_week_dt),
            ('start', '<=', end_of_week_dt),
            ('in_this_week', '=', False)
        ])
        events_this_week.write({'in_this_week': True})
        # 2. Find events more than 1 week ago and in_this_week is True
        one_week_ago = today - timedelta(weeks=1)
        one_week_ago_dt = datetime.combine(one_week_ago, datetime.max.time())  # compare to end of day
        events_past_week = calendar_event.search([
            ('start', '<=', one_week_ago_dt),
            ('in_this_week', '=', True)
        ])
        events_past_week.write({'in_this_week': False})

    @api.depends('stop_date', 'start_date', 'start', 'duration', 'allday')
    def _compute_end_duration(self):
        for record in self:
            if record.allday:
                record.end_duration = record.stop_date.strftime('%B %d, %Y')
            else:
                if record.start and record.duration:
                    start_datetime = fields.Datetime.context_timestamp(record, record.start)
                    end_datetime = start_datetime + timedelta(hours=record.duration)
                    record.end_duration = end_datetime.strftime('%B %d, %Y %H:%M')
                else:
                    record.end_duration = record.start.strftime('%B %d, %Y %H:%M')

    @api.model
    def create(self, vals):
        print('ockehmantag')
        event = super(CalendarEvent, self).create(vals)
        self._cron_update_meeting_status()
        # self.lead_id.update_this_week_meeting()
        return event
    #
    # def write(self, vals):
    #     res = super(CalendarEvent, self).write(vals)
    #     if 'start' in vals or 'res_model' in vals or 'res_id' in vals:
    #         # self.env['crm.lead'].update_this_week_meeting()
    #         self._cron_update_meeting_status()
    #     return res

    @api.depends('recurrence_id', 'recurrency')
    def _compute_recurrence(self):
        recurrence_fields = self._get_recurrent_fields()
        false_values = {field: False for field in recurrence_fields}
        #get default values from calendar.recurrence
        self.env.cr.execute(f"""
            SELECT {', '.join(recurrence_fields)}
            FROM calendar_recurrence LIMIT 1
        """)
        defaults = {field: None for field in recurrence_fields}
        for field in recurrence_fields:
            self.env.cr.execute(f"SELECT {field} FROM calendar_recurrence LIMIT 1")
            result = self.env.cr.fetchone()
            defaults[field] = result[0] if result else False

        for event in self:
            if event.recurrency:
                event_values = event._get_recurrence_params()
                rrule_values = {
                    field: getattr(event.recurrence_id, field)
                    for field in recurrence_fields
                    if getattr(event.recurrence_id, field, False)
                }
                event.update({**false_values, **defaults, **event_values, **rrule_values})
            else:
                event.update(false_values)

    @api.model
    def _get_recurrent_fields(self):
        return {'byday', 'until', 'rrule_type', 'month_by', 'event_tz', 'rrule',
                'interval', 'count', 'end_type', 'mo', 'tu', 'we', 'th', 'fr', 'sa',
                'su', 'day', 'weekday'}

    def create_reschedule_meeting(self):
        result = super(CalendarEvent, self).create_reschedule_meeting()
        result['context'].update({
            'default_resource_type_id': self.resource_type_id.id,
            'default_service_id': self.service_id.id,
            'default_resource_id': self.resource_id.id,
            'default_allday': False,
        })
        return result