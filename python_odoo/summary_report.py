from datetime import timedelta, datetime
import pytz
from odoo import api, fields, models, _
from odoo import tools

def download_report_in_listview(self):
    datas = self._prepare_report_data()
    self._clear_existing_customer_order_dic()
    self._process_orders(datas)
    self._update_wizard_fields(datas)
    # Mendapatkan ID dari tree view yang digunakan untuk menampilkan data
    tree_view_id = self.env.ref('equip3_sale_report.view_list_order_tree').id
    report_display_views = [(tree_view_id, 'tree')]
    return {
        'name': _('Sale Invoice Summary Report'),
        'res_model': 'list.order',
        'domain': [('cust_dic_id', '!=', False)],
        'view_mode': 'tree',
        'type': 'ir.actions.act_window',
        'views': report_display_views,
        'target': 'current',
    }


def _prepare_report_data(self):
    """ Membaca dan menyiapkan data laporan. """
    datas = self.read()[0]
    datas.update(self._get_report_values(datas))
    return datas


def _clear_existing_customer_order_dic(self):
    """ Menghapus data customer_order_dic sebelum diproses ulang. """
    self.write({'customer_order_dic': [(6, 0, [])]})


def _process_orders(self, datas):
    """ Memproses data pesanan untuk setiap pelanggan yang dipilih. """
    order_dic_obj = self.env['customer.order.dic']
    list_order_obj = self.env['list.order']

    for user in datas['sh_partner_ids']:
        name = self.env['res.partner'].browse(user).name
        dic = self._create_order_dic(order_dic_obj, name)

        for line in datas['customer_order_dic'].get(name, []):
            self._create_list_order(list_order_obj, dic.id, line)


def _create_order_dic(self, order_dic_obj, name):
    """ Membuat entri order dictionary untuk seorang salesperson. """
    return order_dic_obj.create({
        'report_id': self.id,
        'saleperson': name,
    })


def _create_list_order(self, list_order_obj, dic_id, line):
    """ Membuat entri detail order untuk seorang salesperson. """
    list_order_obj.create({
        'cust_dic_id': dic_id,
        'order_number': line['order_number'],
        'order_date': line['order_date'],
        'invoice_number': line['invoice_number'],
        'invoice_date': line['invoice_date'],
        'invoice_currency_id': line['invoice_currency_id'],
        'total': line['invoice_amount'],
        'paid_amount': line['invoice_paid_amount'],
        'due_amount': line['due_amount']
    })


def _update_wizard_fields(self, datas):
    """ Memperbarui field wizard dengan data terbaru. """
    self.write({
        'sh_start_date': datas['sh_start_date'],
        'sh_end_date': datas['sh_end_date'],
        'sh_partner_ids': [(6, 0, datas['sh_partner_ids'])],
        'company_ids': [(6, 0, datas['company_ids'])],
        'sh_status': datas['sh_status'],
        'currency_precision': datas['currency_precision']
    })


def _get_report_action(self):
    """ Mengembalikan action untuk mencetak laporan. """
    return self.env.ref('equip3_sale_report.sale_invoice_summary_action').report_action(self)


def print_report(self):
    datas = self._prepare_report_data()
    self._clear_existing_customer_order_dic()
    self._process_orders(datas)
    self._update_wizard_fields(datas)
    return self._get_report_action()


# tambahan
order_number = fields.Char(string="Order Number")
    order_date = fields.Date(string="Order Date")
    total = fields.Monetary(string="Invoice Amount", currency_field='invoice_currency_id')
    paid_amount = fields.Monetary(string="Amount Paid", currency_field='invoice_currency_id')
    due_amount = fields.Monetary(string="Amount Due", currency_field='invoice_currency_id')