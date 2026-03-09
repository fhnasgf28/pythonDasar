def print_report(self):
    order_dic_obj = self.env['customer.order.dic']
    list_order_obj = self.env['list.order']
    datas = self.read()[0]
    datas.update(self._get_report_values(datas))
    self.write({
        'customer_order_dic': [(6, 0, [])]
    })
    for user in datas['sh_partner_ids']:
        name = self.env['res.partner'].browse(user).name
        dic = order_dic_obj.create({
            'report_id': self.id,
            'saleperson': name,
        })
        for line in datas['customer_order_dic'][name]:
            list_order_obj.create({
                'cust_dic_id': dic.id,
                'order_number': line['order_number'],
                'order_date': line['order_date'],
                'invoice_number': line['invoice_number'],
                'invoice_date': line['invoice_date'],
                'invoice_currency_id': line['invoice_currency_id'],
                'total': line['invoice_amount'],
                'paid_amount': line['invoice_paid_amount'],
                'due_amount': line['due_amount']
            })
    self.write({
        'sh_start_date': datas['sh_start_date'],
        'sh_end_date': datas['sh_end_date'],
        'sh_partner_ids': [(6, 0, datas['sh_partner_ids'])],
        'company_ids': [(6, 0, datas['company_ids'])],
        'sh_status': datas['sh_status'],
        'currency_precision': datas['currency_precision']
    })
