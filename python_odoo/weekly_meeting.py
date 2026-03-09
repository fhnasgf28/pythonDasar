check_this_week_has_meeting = fields.Boolean(string='Check This Week Has Meeting',
                                                 compute='_compute_this_week_meeting', store=False)
    this_week_has_meeting = fields.Boolean(string='This Week Has Meeting')


    @api.depends('meeting_ids', 'meeting_count',
                 'meeting_ids.start',
                 'meeting_ids.start_date')
    def _compute_this_week_meeting(self):
        for lead in self:
            today = datetime.now()
            start_of_week = today - timedelta(days=today.weekday())  # Awal minggu
            end_of_week = start_of_week + timedelta(days=6)  # Akhir minggu

            meetings = lead.meeting_ids.filtered(
                lambda event: start_of_week.date() <= event.start.date() <= end_of_week.date()
            )
            lead.check_this_week_has_meeting = bool(meetings)
            lead.this_week_has_meeting = bool(meetings)
            print(f"lead: {lead.name}, meeting this week : {meetings.mapped('name')}")
            print(f"bagaimana hasil kodingan ini", lead.this_week_has_meeting)