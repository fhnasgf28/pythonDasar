store = True, help = "Time duration (in days) from first meeting to stage change")
check_this_week_has_meeting = fields.Boolean(string='Check This Week Has Meeting',
                                             compute='_compute_check_this_week_has_meeting')
this_week_has_meeting = fields.Boolean(string='This Week Has Meeting')


def _get_start_end_of_week(self, date_in_week):
    start_of_week = date_in_week - timedelta(days=date_in_week.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    return start_of_week, end_of_week


def _compute_check_this_week_has_meeting(self):
    today = date.today()
    start_of_week, end_of_week = self._get_start_end_of_week(today)
    start_of_week = fields.Date.to_string(start_of_week)
    print('kodingan ini gimana', start_of_week)
    end_of_week = fields.Date.to_string(end_of_week)
    print('kodingan ini oke saja', end_of_week)

    for lead in self:
        meeting = self.env['calendar.event'].search([
            ('start_date', '>=', start_of_week),
            ('start_date', '<=', end_of_week),
        ])
        print('berapa total kogingan ini', len(meeting))
        if meeting:
            lead.this_week_has_meeting = bool(meeting)
            lead.check_this_week_has_meeting = bool(meeting)


@api.model
def create(self, vals):
    lead = super(CRMLead, self).create(vals)
    lead._compute_check_this_week_has_meeting
    if lead.meeting_ids:
        lead.first_meeting_date = min(lead.meeting_ids.mapped('start'))
    return lead