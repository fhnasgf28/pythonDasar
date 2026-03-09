# follow up leads per week or day
def _check_activity_today(self, activity):
    if activity.date_deadline == Date.context_today(self):
        lead = self.env['crm.lead'].browse(activity.res_id)
        if lead:
            lead._get_leads_to_follow_up(time_range='day')

    #
    # def write(self, vals):
    #     res = super(CalendarEvent, self).write(vals)
    #     if 'start' in vals or 'res_model' in vals or 'res_id' in vals:
    #         # self.env['crm.lead'].update_this_week_meeting()
    #         self._cron_update_meeting_status()
    #     return res

