@api.depends('recurrence_id', 'recurrency')
def _compute_recurrence(self):
    recurrence_fields = self._get_recurrent_fields()
    false_values = {field: False for field in recurrence_fields}
    defaults = self.env['calendar.recurrence'].default_get(recurrence_fields)

    # Pre-fetch recurrence_id data for all events
    events_with_recurrence = self.filtered('recurrence_id')
    recurrence_data = events_with_recurrence.recurrence_id.read(recurrence_fields)
    recurrence_data_by_id = {data['id']: data for data in recurrence_data}

    for event in self:
        if event.recurrency:
            event_values = event._get_recurrence_params()

            # Use pre-fetched data instead of accessing event.recurrence_id repeatedly
            rrule_values = {
                field: recurrence_data_by_id[event.recurrence_id.id][field]
                for field in recurrence_fields
                if recurrence_data_by_id[event.recurrence_id.id][field]
            }

            event.update({**false_values, **defaults, **event_values, **rrule_values})
        else:
            event.update(false_values)