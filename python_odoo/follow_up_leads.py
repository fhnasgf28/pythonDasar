#follow up lead
    def _get_leads_to_follow_up(self, time_range='week'):
        """
        Mengambil leads yang memiliki aktivitas dalam jangka waktu tertentu.
        """
        today = fields.Date.today()
        domain = [('res_model', '=', 'crm.lead'), ('res_id', 'in', self.ids)]

        if time_range == 'day':  # Filter aktivitas harian
            domain += [('date_deadline', '=', today)]
        elif time_range == 'week':  # Filter aktivitas mingguan
            start_week = today - timedelta(days=today.weekday())
            end_week = start_week + timedelta(days=6)
            domain += [('date_deadline', '>=', start_week), ('date_deadline', '<=', end_week)]

        activities = self.env['mail.activity'].search(domain)
        lead_ids = activities.mapped('res_id')
        return self.browse(lead_ids)

    @api.depends('activity_ids.date_deadline')
    def _compute_has_activity_today(self):
        today = fields.Date.today()
        for lead in self:
            activities = lead.activity_ids.filtered(lambda a: a.date_deadline == today)
            lead.has_activity_today = bool(activities)

    @api.depends('activity_ids.date_deadline')
    def _compute_has_activity_this_week(self):
        today = fields.Date.today()
        start_week = today - timedelta(days=today.weekday())
        end_week = start_week + timedelta(days=6)
        for lead in self:
            activities = lead.activity_ids.filtered(
                lambda a: a.date_deadline and start_week <= a.date_deadline <= end_week
            )
            lead.has_activity_this_week = bool(activities)