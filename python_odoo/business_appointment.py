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