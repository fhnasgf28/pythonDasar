from odoo import models, fields, api
from datetime import datetime, time

class BlanketOrder(models.Model):
    _name = 'blanket.order'
    _description = 'Blanket Order'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    order_date = fields.Date(string='Order Date', required=True)
    delivery_date = fields.Date(string='Delivery Date', required=True)
    customer_id = fields.Many2one('res.partner', string='Customer', required=True)
    order_lines = fields.One2many('blanket.order.line', 'order_id', string='Order Lines')

    # 2. Debug log sebelum disimpan
    def create(self, vals):
        print("\n=========== DEBUG CREATE ===========")
        print("Original vals:", vals)
        print("Original date_end (raw):", vals.get('date_end'))
        # Ensure date_end always has time set to 12:00 PM if provided
        # Atur date_end ke jam 12 siang waktu lokal user
        if vals.get('date_end'):
            date_end = vals['date_end']
            if isinstance(date_end, str):
                date_end = fields.Datetime.from_string(date_end)
            # Set jam UTC-nya ke 05:00:00 (agar tampil jam 12 siang WIB)
            date_end_utc = datetime.combine(date_end.date(), time(hour=5, minute=0, second=0))
            vals['date_end'] = date_end_utc
            print("Set date_end (jam 5 UTC untuk 12 siang WIB):", vals['date_end'])
        # if vals.get('date_end'):
        #     user = self.env.user
        #     tz = pytz.timezone(user.tz or 'UTC')
        #
        #     date_end = vals['date_end']
        #     if isinstance(date_end, str):
        #         date_end = fields.Datetime.from_string(date_end)
        #
        #     # Buat tanggal dengan jam 12 siang
        #     local_noon = datetime.combine(date_end.date(), datetime.min.time().replace(hour=12))
        #     # Lokalisasi ke timezone user
        #     local_noon_tz = tz.localize(local_noon)
        #     # Konversi ke UTC
        #     utc_noon = local_noon_tz.astimezone(pytz.UTC)
        #     # Hapus informasi timezone (naive UTC)
        #     vals['date_end'] = utc_noon.replace(tzinfo=None)
        #
        #     print("Final date_end after conversion:", vals['date_end'])

        return super(BlanketOrder, self).create(vals)


    def write(self, vals):
    # Ensure date_end always has time set to 12:00 PM if provided
        if vals.get('date_end'):
            date_end = vals['date_end']
            if isinstance(date_end, str):
                date_end = fields.Datetime.from_string(date_end)
            if isinstance(date_end, datetime) and (date_end.hour != 12 or date_end.minute != 0 or date_end.second != 0):
                # Set time to 12:00 PM while preserving the date
                date_end = date_end.replace(hour=12, minute=0, second=0, microsecond=0)
                vals['date_end'] = date_end

        return super(BlanketOrder, self).write(vals)
