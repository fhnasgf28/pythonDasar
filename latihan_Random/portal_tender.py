@http.route(['/export-tender-portal-rfq'], type='http', auth="public", website=True)
    def download_template_import_member_point_rfq(self, **post):

        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet('Sheet 1')
        rec_ids = list(map(int, post['ids'].split(',')))
        title_style_center = workbook.add_format(
            {'bold': True, 'font_size': 13, 'align': 'center', 'valign': 'vcenter'})
        style_center = workbook.add_format({'bold': False, 'font_size': 11, 'align': 'center', 'valign': 'vcenter'})
        worksheet.set_column(0, 25, 30)
        purchase_sudo = request.env['purchase.order'].sudo()
        tenders = purchase_sudo.browse(rec_ids)

        worksheet.write(0, 0, 'Name', title_style_center)
        worksheet.write(0, 1, 'Tender Name', title_style_center)
        worksheet.write(0, 2, 'Tender Scope', title_style_center)
        worksheet.write(0, 3, 'Tender Deadline', title_style_center)
        worksheet.write(0, 4, 'Purchase Agreement Line/ID', title_style_center)
        worksheet.write(0, 5, 'Purchase Agreement Line/Product', title_style_center)
        worksheet.write(0, 6, 'Purchase Agreement Line/Description', title_style_center)
        worksheet.write(0, 7, 'Purchase Agreement Line/Quantity', title_style_center)
        worksheet.write(0, 8, 'Purchase Agreement Line/UoM', title_style_center)
        worksheet.write(0, 9, 'Purchase Agreement Line/Unit Price', title_style_center)
        worksheet.write(0, 10, 'Purchase Order/Purchase Order Lines/Unit Price', title_style_center)
        worksheet.write(0, 0, 'Name', title_style_center)
        worksheet.write(0, 11, 'Tender Name', title_style_center)
        worksheet.write(0, 12, 'Tender Scope', title_style_center)
        worksheet.write(0, 13, 'Tender Deadline', title_style_center)
        worksheet.write(0, 14, 'Purchase Agreement Line/ID', title_style_center)
        worksheet.write(0, 15, 'Purchase Agreement Line/Product', title_style_center)
        worksheet.write(0, 16, 'Purchase Agreement Line/Description', title_style_center)
        worksheet.write(0, 17, 'Purchase Agreement Line/Quantity', title_style_center)
        worksheet.write(0, 18, 'Purchase Agreement Line/UoM', title_style_center)
        worksheet.write(0, 19, 'Purchase Agreement Line/Unit Price', title_style_center)
        worksheet.write(0, 20, 'Purchase Order/Purchase Order Lines/Unit Price', title_style_center)
        count = 1
        for tender in tenders:
            date_deadline = ''
            if tender.sh_agreement_deadline:
                date_deadline = tender.sh_agreement_deadline.strftime("%Y-%m-%d %H:%M:%S")
            tender_scope = ''
            if tender.tender_scope:
                tender_scope = dict(tender._fields['tender_scope'].selection).get(tender.tender_scope, '')
            worksheet.write(count, 0, tender.name or '', style_center)
            worksheet.write(count, 1, tender.tender_name or '', style_center)
            worksheet.write(count, 2, tender_scope or '', style_center)
            worksheet.write(count, 3, date_deadline or '', style_center)
            count_line = 0
            for pal in tender.sh_purchase_agreement_line_ids:
                count_line += 1
                worksheet.write(count, 4, pal.id or '', style_center)
                worksheet.write(count, 5, pal.sh_product_id.display_name or '', style_center)
                worksheet.write(count, 6, pal.sh_product_description or '', style_center)
                worksheet.write(count, 7, pal.sh_qty or '', style_center)
                worksheet.write(count, 8, pal.sh_product_uom_id.display_name or '', style_center)
                worksheet.write(count, 9, pal.sh_price_unit or '', style_center)
                if count_line != len(tender.sh_purchase_agreement_line_ids):
                    count += 1
            count += 1

        name_file = 'Export RFQ Documents'
        workbook.close()
        xlsx_data = output.getvalue()
        response = request.make_response(
            xlsx_data,
            headers=[('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
                     ('Content-Disposition', 'attachment; filename=%s.xlsx' % name_file)]
        )

        return response
