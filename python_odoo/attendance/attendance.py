from odoo import models, fields, api
from datetime import datetime, timedelta
import pytz

class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    total_hours = fields.Float(string='Total Hours', compute='_compute_total_hours')
    total_valid_hours = fields.Float(string="Total Jam Kerja (Valid)", compute="_compute_attendance_metrics")
    total_late_minutes = fields.Float(string="Total Keterlambatan (menit)", compute="_compute_attendance_metrics")


    @api.depends('attendance_ids.check_in', 'attendance_ids.check_out')
    def _compute_total_hours(self):
        for employee in self:
            total_duration = timedelta()
            print(total_duration)
            attendance = self.env['hr.attendance'].search([('employee_id', '=', employee.id)])
            for att in attendance:
                if att.check_in and att.check_out:
                    total_duration += att.check_out - att.check_in
            employee.total_hours = total_duration.total_seconds() / 3600
    
    # Filter hanya bulan ini atau minggu ini
    def this_month(self):
        return self.env['hr.attendance'].search([('employee_id', '=', self.id), ('check_in', '>=', datetime.now().replace(day=1)), ('check_in', '<=', datetime.now().replace(day=31))])
    
    @api.depends('attendance_ids.check_in', 'attendance_ids.check_out')
    def _compute_attendance_metrics(self):
        for employee in self:
            total_valid_duration = timedelta()
            total_late_minutes = 0.0

            # get tanggal hari ini
            today = fields.Date.today()
            start_of_month = today.replace(day=1)
            start_of_week = today - timedelta(days=today.weekday()) #monday

            filter_start_date = start_of_month

            # ambil semua attendance dalam periode 
            attendances = self.env['hr.attendance'].search([
                ('employee_id', '=', employee.id), 
                ('check_in', '>=', filter_start_date),
                ('check_out', '!=', False)
            ])

            for att in attendances:
                check_in = att.check_in
                check_out = att.check_out 

                # hitung jam kerja
                duration = check_out - check_in
                hours = duration.total_seconds() / 3600

                # ambil hanya jam kerja > 5 jam
                if hours > 5:
                    total_valid_duration += duration
                
                # hitung keterlambatan dari jam kerja ideal (jam 08.00 - 17.00)
                ideal_checkin_time = check_in.replace(hour=8, minute=0, second=0)
                if check_in < ideal_checkin_time:
                    delay = check_in - ideal_checkin_time
                    total_late_minutes += delay.total_seconds() / 60

            employee.total_valid_hours = total_valid_duration.total_seconds() / 3600
            employee.total_late_minutes = total_late_minutes
    

