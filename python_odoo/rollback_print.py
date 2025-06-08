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
    list_order_ids = []

    for user in datas['sh_partner_ids']:
        name = self.env['res.partner'].browse(user).name
        dic = self._create_order_dic(order_dic_obj, name)

        for line in datas['customer_order_dic'].get(name, []):
            list_order = self._create_list_order(list_order_obj, dic.id, line)
            list_order_ids.append(list_order.id)
    self.write({'list_order_ids': [(6, 0, list_order_ids)]})


def _create_order_dic(self, order_dic_obj, name):
    """ Membuat entri order dictionary untuk seorang salesperson. """
    return order_dic_obj.create({
        'report_id': self.id,
        'saleperson': name,
    })


def _create_list_order(self, list_order_obj, dic_id, line):
    """ Membuat entri detail order untuk seorang salesperson. """
    return list_order_obj.create({
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
