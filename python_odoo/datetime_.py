@api.constrains('start_date', 'stop_date', 'resource_id', 'resource_type_id', 'service_id')
    def _check_dates(self):
        for event in self:
            if event.start_date and event.stop_date and event.resource_id and event.resource_type_id and event.service_id:
                for resource in event.resource_id:
                    # Convert start and stop to date
                    start_date = event.start_date
                    stop_date = event.stop_date

                    domain = [
                        ('start_datetime', '<=', fields.Datetime.to_datetime(str(stop_date) + ' 23:59:59')),
                        ('stop_datetime', '>=', fields.Datetime.to_datetime(str(start_date) + ' 00:00:00')),
                        ('resource_id', 'in', [resource.id]),
                        ('resource_type_id', '=', event.resource_type_id.id),
                        ('service_id', '=', event.service_id.id),
                    ]

                    # Exclude current business appointment if updating existing record.
                    if event.business_appointment_id:
                        domain.append(('id', '!=', event.business_appointment_id.id))

                    if self.env['business.appointment'].search_count(domain) > 0:
                        raise ValidationError(
                            f"Duplicate schedule detected in Business Appointment for resource: {resource.name} "
                            f"with the same start date, stop date, resource type, and service!"
                        )