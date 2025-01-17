@api.depends('recurrence_id', 'recurrency')
def _compute_recurrence(self):
    print('Optimizing _compute_recurrence')
    recurrence_fields = self._get_recurrent_fields()
    false_values = {field: False for field in recurrence_fields}  # Fields default to False
    defaults = self.env['calendar.recurrence'].default_get(recurrence_fields)

    recurrency_events = self.filtered(lambda e: e.recurrency)
    if not recurrency_events:
        return
    recurrence_ids = recurrency_events.mapped('recurrence_id.id')

    self.env.cr.execute(f"""
               SELECT id, {', '.join(recurrence_fields)}
               FROM calendar_recurrence
               WHERE id = ANY(%s)
           """, (recurrence_ids,))
    recurrence_data = {rec['id']: rec for rec in self.env.cr.dictfetchall()}

    for event in recurrency_events:
        recurrence_id = event.recurrence_id.id
        if recurrence_id in recurrence_data:
            rrule_values = {
                field: recurrence_data[recurrence_id].get(field)
                for field in recurrence_fields
                if recurrence_data[recurrence_id].get(field) is not None
            }
            event_values = event._get_recurrence_params()
            event.update({**false_values, **defaults, **event_values, **rrule_values})
        else:
            # Jika tidak ada recurrence, reset ke default
            event.update(false_values)