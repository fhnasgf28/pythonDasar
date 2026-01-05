from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import xlwt
import operator
import base64
from io import BytesIO
import pytz
from datetime import datetime, timedelta
from odoo.tools.misc import DEFAULT_SERVER_DATETIME_FORMAT
from odoo.tools import float_is_zero

class TopVendorReport(models.AbstractModel):
    _inherit = 'top.vendor.report'

    @api.model
    def _get_report_values(self, docids, data=None):
        data = dict(data or {})
        purchase_order_obj = self.env['purchase.order']
        currency_id = False
        basic_date_start = False
        basic_date_stop = False
        if data['date_from']:
            basic_date_start = fields.Datetime.from_string(data['date_from'])
        else:
            user_tz = pytz.timezone(self.env.context.get('tz') or self.env.user.tz or 'UTC')
            today = user_tz.localize(fields.Datetime.from_string(fields.Date.context_today(self)))
            basic_date_start = today.astimezone(pytz.timezone('UTC'))

        if data['date_to']:
            basic_date_stop = fields.Datetime.from_string(data['date_to'])
            if (basic_date_stop < basic_date_start):
                basic_date_stop = basic_date_start + timedelta(days=1, seconds=-1)
        else:
            basic_date_stop = basic_date_start + timedelta(days=1, seconds=-1)

        domain = [
            ('order_id.state', 'in', ['purchase', 'done'])
        ]
        if data.get('company_ids', False):
            domain.append(('order_id.company_id', 'in', data.get('company_ids', False)))
        if data.get('date_from', False):
            domain.append(('order_id.date_order', '>=',fields.Datetime.to_string(basic_date_start)))
        if data.get('date_to', False):
            domain.append(('order_id.date_order', '<=', fields.Datetime.to_string(basic_date_stop)))

        search_order_lines = purchase_order_obj.sudo().search(domain)
        product_total_qty_dic = {}
        if search_order_lines:
            for line in search_order_lines.sorted(key=lambda o: o.product_id.id):
                if product_total_qty_dic.get(line.product_id.name, False):
                    qty = product_total_qty_dic.get(line.product_id.name)
                    qty += line.product_qty
                    product_total_qty_dic.update({line.product_id.name: qty})
                else:
                    product_total_qty_dic.update(
                        {line.product_id.name: line.product_qty}
                    )
        final_compare_product_list = []
        final_compare_product_qty_list = []
        if product_total_qty_dic:
            sorted_product_total_qty_list = sorted(
                product_total_qty_dic.items(), key=operator.itemgetter(1)
            )
            counter = 0

            for tuple_item in sorted_product_total_qty_list:
                if data['product_qty'] != 0 and tuple_item[1] >= data['product_qty']:
                    final_compare_product_list.append(tuple_item[0])
                elif data['product_qty'] == 0:
                    final_compare_product_list.append(tuple_item[0])

                final_compare_product_qty_list.append(tuple_item[1])
                counter += 1
                if counter >= data['no_of_top_item']:
                    break

    def print_report(self):
        start_date_str = False
        end_date_str = False
        if self.start_date:
            local_start_date = fields.Datetime.context_timestamp(self, self.start_date)
            start_date_str = local_start_date.strftime('%Y-%m-%d %H:%M:%S')
        if self.end_date:
            local_end_date = fields.Datetime.context_timestamp(self, self.end_date)
            end_date_str = local_end_date.strftime('%Y-%m-%d %H:%M:%S')
        display_start_date = fields.Datetime.context_timestamp(self, self.start_date).strftime(
            '%d %B %Y') if self.start_date else ''
        display_end_date = fields.Datetime.context_timestamp(self, self.end_date).strftime(
            '%d %B %Y') if self.end_date else ''
        datas = {
            'date_start': display_start_date,
            'date_stop': display_end_date,
            'res_date_start': start_date_str or '',
            'res_date_stop': end_date_str or '',
            'company_id': self.company_ids.ids,
            'state': self.state,
            'branch_ids': self.branch_ids.ids
        }
        return self.env.ref('sh_purchase_reports.sh_purchase_details_report_action').report_action([], data=datas)

