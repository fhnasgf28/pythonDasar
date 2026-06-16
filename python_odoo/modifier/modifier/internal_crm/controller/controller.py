from odoo import http
from odoo.http import request

class CalendarEventController(http.Controller):
    @http.route('/get/calendar/event/details', type='json', auth='user')
    def get_calendar_event_details(self, event_id):
        print('kodingan ini dieksekusi')
        event = request.env['calendar.event'].browse(int(event_id))
        print('ini kodingan event')
        if event.exists():
            return {
                'name': event.name,
                'start': event.start,
                'stop': event.stop,
                'description': event.description,
                'privacy': event.privacy,
                'user_id': event.user_id.name if event.user_id else None,
            }
        return False