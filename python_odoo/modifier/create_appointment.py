@api.model
    def create(self, vals_list):
        events = super(CalendarEvent, self).create(vals_list)
        for event, vals in zip(events, vals_list):
            if not event.business_appointment_id:
                appointment_vals = self._prepare_appointment_vals(event)
                appointment = self.env['business.appointment'].create(appointment_vals)
                event.business_appointment_id = appointment.id
        return events

    def _prepare_appointment_vals(self, event):
        """
        Prepare the values for creating a business.appointment.
        """
        partner = event.partner_id.id if event.partner_id else False
        # Tentukan datetime_end berdasarkan kondisi allday
        datetime_end = (
            event.stop_date if event.allday
            else fields.Datetime.to_datetime(event.start) + timedelta(hours=event.duration)
        )

        return {
            'name': event.name,
            'datetime_start': event.start_date if event.allday else event.start,
            'datetime_end': datetime_end,
            'calendar_event_id': event.id,
            'partner_id': partner,
            'resource_id': event.resource_id.id,
            'resource_type_id': event.resource_type_id.id,
            'service_id': event.service_id.id,
        }

    @api.constrains('start_date', 'stop_date', 'resource_id', 'resource_type_id', 'service_id')
    def _check_dates(self):
        for event in self:
            if event.start_date and event.stop_date and event.resource_id and event.resource_type_id and event.service_id:
                if event.allday:
                    start_datetime = fields.Datetime.to_datetime(event.start_date)
                    stop_datetime = fields.Datetime.to_datetime(event.stop_date)
                else:
                    start_datetime = event.start
                    stop_datetime = fields.Datetime.to_datetime(event.start) + timedelta(hours=event.duration)
                for resource in event.resource_id:
                    domain = [
                        ('datetime_start', '=', start_datetime),
                        ('datetime_end', '=', stop_datetime),
                        ('resource_type_id', '=', event.resource_type_id.id),
                        ('service_id', '=', event.service_id.id),
                    ]
                    if self.env['business.appointment'].search_count(domain) > 0:
                        raise ValidationError(
                            f"Duplicate schedule detected in Business Appointment for resource: {resource.name} "
                            f"with the same start date, stop date, resource type, and service!"
                        )
