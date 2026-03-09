@api.model
    def update_this_week_meeting(self):
        """Cron job to update the 'this_week_meeting' field"""
        print('method ini kena triger')
        today = fields.Date.today()
        print('ini adalah today ',today)
        start_of_week = today - timedelta(days=today.weekday()) #monday
        end_of_week = start_of_week + timedelta(days=6)

        #find records with meetings this week
        self.env.cr.execute('''
                   SELECT DISTINCT res_id
                   FROM calendar_event
                   WHERE start >= %s AND start <= %s AND res_id IS NOT NULL AND res_model = 'crm.lead'
               ''', (start_of_week, end_of_week))
        leads_with_meetings = [row[0] for row in self.env.cr.fetchall()]

        # Update `this_week_meeting` field efficiently
        self.env.cr.execute('''
                    UPDATE crm_lead
                    SET this_week_has_meeting = CASE
                        WHEN id = ANY(%s) AND %s <= %s THEN TRUE
                        ELSE FALSE
                    END
                ''', (leads_with_meetings, today, end_of_week))