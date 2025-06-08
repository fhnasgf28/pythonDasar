def generate_report_data(self):
    datas = self.read()[0]
    product_detail_data = self.get_product()
    total_per_day = {
        'monday': sum([t.get('monday', 0) or 0 for t in product_detail_data]),
        'tuesday': sum([t.get('tuesday', 0) or 0 for t in product_detail_data]),
        'wednesday': sum([t.get('wednesday', 0) or 0 for t in product_detail_data]),
        'thursday': sum([t.get('thursday', 0) or 0 for t in product_detail_data]),
        'friday': sum([t.get('friday', 0) or 0 for t in product_detail_data]),
        'saturday': sum([t.get('saturday', 0) or 0 for t in product_detail_data]),
        'sunday': sum([t.get('sunday', 0) or 0 for t in product_detail_data]),
    }
    grand_total = sum(total_per_day.values())
    data = {'date_start': self.start_date.strftime('%d %B %Y'), 'date_stop': self.end_date.strftime('%d %B %Y'),
            'company_ids': self.company_ids.ids,
            'product_detail_data': self.get_product(),
            'total_per_day': total_per_day,
            'grand_total': grand_total,
            }
    return self.env.ref('sh_purchase_reports.action_report_purchase_order_day_wise_report').report_action([], data=data)