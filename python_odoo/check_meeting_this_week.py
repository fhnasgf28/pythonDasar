check_meeting_ids = fields.Many2many(
        'calendar.event',
        string='Meetings This Week',
        compute='_compute_meetings_this_week'
    )

    this_week_has_meeting = fields.Boolean(
        string='This Week Has Meeting',
    )

    def _get_start_end_of_week(self, date_in_week):
        start_of_week = date_in_week - timedelta(days=date_in_week.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        return start_of_week, end_of_week

    @api.depends('user_id')  # Trigger recompute when 'user_id' changes
    def _compute_meetings_this_week(self):
        today = date.today()
        start_of_week, end_of_week = self._get_start_end_of_week(today)

        # Convert to datetime objects for comparison with 'start' and 'stop' fields
        start_of_week_dt = datetime.combine(start_of_week, datetime.min.time())
        end_of_week_dt = datetime.combine(end_of_week, datetime.max.time())

        for lead in self:
            domain = [
                ('start', '<=', end_of_week_dt),
                ('stop', '>=', start_of_week_dt),
                '|',
                ('partner_ids', 'in', lead.partner_id.ids if lead.partner_id else []),
                # Check if the lead's partner is in the meeting's attendees
                ('user_id', '=', lead.user_id.id if lead.user_id else False),
                # Check if the lead's assigned user is the organizer
            ]
            meetings = self.env['calendar.event'].search(domain)

            lead.check_meeting_ids = meetings
            lead.this_week_has_meeting = bool(meetings)

    def get_meetings_this_week(self):
        """
        Returns the calendar.event records for the current week related to the lead.
        """
        today = date.today()
        start_of_week, end_of_week = self._get_start_end_of_week(today)
        start_of_week_dt = datetime.combine(start_of_week, datetime.min.time())
        end_of_week_dt = datetime.combine(end_of_week, datetime.max.time())

        domain = [
            ('start', '<=', end_of_week_dt),
            ('stop', '>=', start_of_week_dt),
            '|',
            ('partner_ids', 'in', self.partner_id.ids if self.partner_id else []),
            ('user_id', '=', self.user_id.id if self.user_id else False),
        ]

        return self.env['calendar.event'].search(domain)