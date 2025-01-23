# follow up leads per week or day
def _check_activity_today(self, activity):
    if activity.date_deadline == Date.context_today(self):
        lead = self.env['crm.lead'].browse(activity.res_id)
        if lead:
            lead._get_leads_to_follow_up(time_range='day')