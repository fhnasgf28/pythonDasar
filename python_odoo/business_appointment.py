@api.constrains('start_datetime', 'stop_datetime')
    def _check_dates(self):
        print('kodingan ini kena ekpedisi')
        for appointment in self:
            if appointment.datetime_start and appointment.datetime_end:
                if self.check_overlap(appointment.datetime_start, appointment.datetime_end, appointment.id):
                    raise ValidationError("Konflik jadwal terdeteksi di Business Appointment!")
                if appointment.calendar_event_id:
                    if self.env['calendar.event'].search_count([
                        ('start_date', '<', appointment.datetime_end),
                        ('stop_date', '>', appointment.datetime_start),
                        ('id', '!=', appointment.calendar_event_id.id)
                    ]) > 0:
                        raise ValidationError("Konflik jadwal terdeteksi di Calendar Event!")


def check_overlap(self, start_date, stop_date, resource_id=None, exclude_id=None):
    print(
        f'Checking overlap: start_date={start_date}, stop_date={stop_date}, resource_id={resource_id}, exclude_id={exclude_id}')
    domain = [
        ('datetime_start', '<', stop_date),
        ('datetime_end', '>', start_date),
    ]
    if resource_id:
        domain.append(('resource_id', '=', resource_id))
    if exclude_id:
        domain.append(('id', '!=', exclude_id))

    result_count = self.search_count(domain)
    print(f'Overlap count: {result_count}')  # Debugging jumlah hasil pencarian
    return result_count > 0