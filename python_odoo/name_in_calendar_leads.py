display_name_with_stop = fields.Char(
        compute='_compute_display_name_with_stop',
        string="Event Display with Stop"
    )

    @api.depends('name', 'stop')
    def _compute_display_name_with_stop(self):
        for record in self:
            if record.stop:
                record.display_name_with_stop = f"{record.name} (Ends: {record.stop.strftime('%Y-%m-%d %H:%M')})"
            else:
                record.display_name_with_stop = record.name