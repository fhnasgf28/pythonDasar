# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

import io
import xlsxwriter
from odoo import http, fields
from odoo.http import request


class RFQExportController(http.Controller):

    @http.route(['/my/rfq/export'], type='http', auth="user", website=True, csrf=True)
    def export_selected_rfqs(self, **post):
        """Export selected RFQs to Excel file"""
        # Get the selected RFQ IDs from the form submission
        rfq_ids = []

        # First try to get IDs from the consolidated hidden field
        if post.get('selected_rfq_ids'):
            rfq_ids = [int(id) for id in post.get('selected_rfq_ids').split(',') if id]
        else:
            # Fallback to individual checkbox values
            for key, value in post.items():
                if key.startswith('rfq_ids[]') and value:
                    rfq_ids.append(int(value))

        if not rfq_ids:
            return request.redirect('/my/rfq')

        # Create Excel file
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})

        # Create worksheets for RFQ summary and product details
        rfq_sheet = workbook.add_worksheet('RFQs')

        # Define formats for headers and data cells
        title_style = workbook.add_format({
            'bold': True,
            'font_size': 13,
            'align': 'center',
            'valign': 'vcenter',
            'bg_color': '#D3D3D3',
            'border': 1
        })

        data_style = workbook.add_format({
            'font_size': 11,
            'align': 'left',
            'valign': 'vcenter'
        })

        number_style = workbook.add_format({
            'font_size': 11,
            'align': 'right',
            'num_format': '#,##0.00'
        })

        date_style = workbook.add_format({
            'font_size': 11,
            'align': 'center',
            'num_format': 'yyyy-mm-dd'
        })

        # Set column widths for better readability
        rfq_sheet.set_column(0, 0, 20)  # Name/RFQ Reference
        rfq_sheet.set_column(1, 1, 30)  # Partner
        rfq_sheet.set_column(2, 2, 15)  # Currency
        rfq_sheet.set_column(3, 3, 20)  # Date Planned
        rfq_sheet.set_column(4, 4, 20)  # PO Expiry Date
        rfq_sheet.set_column(5, 5, 25)  # User/Purchase Representative
        rfq_sheet.set_column(6, 6, 25)  # Destination Warehouse
        rfq_sheet.set_column(7, 7, 20)  # Branch
        rfq_sheet.set_column(8, 14, 15)  # Boolean fields and other IDs
        rfq_sheet.set_column(15, 15, 20)  # Product
        rfq_sheet.set_column(16, 16, 15)  # Quantity
        rfq_sheet.set_column(17, 17, 15)  # UoM
        rfq_sheet.set_column(18, 18, 15)  # Price Unit
        rfq_sheet.set_column(19, 19, 20)  # Taxes
        rfq_sheet.set_column(20, 20, 20)  # Analytic Tags

        # Get RFQ records with proper access rights
        purchase_sudo = request.env['purchase.order'].sudo()
        rfqs = purchase_sudo.browse(rfq_ids)

        # Apply multi-company filtering if needed
        if request.env.context.get('allowed_company_ids'):
            if len(request.env.companies) == 1:
                rfqs = rfqs.filtered(lambda r: r.company_id.id == request.env.company.id)
            else:
                rfqs = rfqs.filtered(lambda r: r.company_id.id in request.env.companies.ids)

        # Write RFQ sheet headers
        rfq_headers = [
            'Name', 'Partner', 'Currency', 'Date Planned', 'PO Expiry Date',
            'Purchase Representative', 'Destination Warehouse', 'Branch',
            'Is Goods Order', 'Is Services Order', 'Is Assets Order', 'Is Rental Order',
            'Milestone Template', 'Analytic Account Groups', 'Payment Term',
            'Product', 'Quantity', 'UoM', 'Price Unit', 'Taxes', 'Analytic Tags'
        ]

        for col, header in enumerate(rfq_headers):
            rfq_sheet.write(0, col, header, title_style)

        # Write RFQ data with product lines on the same sheet
        row = 1
        for rfq in rfqs:
            lines = rfq.order_line or [False]
            # Write RFQ header information only for the first line
            rfq_sheet.write(row, 0, rfq.name or '', data_style)
            rfq_sheet.write(row, 1, rfq.partner_id.name or '', data_style)
            rfq_sheet.write(row, 2, rfq.currency_id.name or '', data_style)
            rfq_sheet.write(row, 3, rfq.date_planned.strftime('%Y-%m-%d') if rfq.date_planned else '', date_style)
            rfq_sheet.write(row, 4, rfq.po_expiry_date.strftime('%Y-%m-%d') if hasattr(rfq,
                                                                                       'po_expiry_date') and rfq.po_expiry_date else '',
                            date_style)
            rfq_sheet.write(row, 5, rfq.user_id.name or '', data_style)
            rfq_sheet.write(row, 6,
                            rfq.picking_type_id.warehouse_id.name if rfq.picking_type_id and rfq.picking_type_id.warehouse_id else '',
                            data_style)
            rfq_sheet.write(row, 7, rfq.branch_id.name if hasattr(rfq, 'branch_id') and rfq.branch_id else '',
                            data_style)
            rfq_sheet.write(row, 8, 'Yes' if hasattr(rfq, 'is_goods_orders') and rfq.is_goods_orders else 'No',
                            data_style)
            rfq_sheet.write(row, 9, 'Yes' if hasattr(rfq, 'is_services_orders') and rfq.is_services_orders else 'No',
                            data_style)
            rfq_sheet.write(row, 10, 'Yes' if hasattr(rfq, 'is_assets_orders') and rfq.is_assets_orders else 'No',
                            data_style)
            rfq_sheet.write(row, 11, 'Yes' if hasattr(rfq, 'is_rental_orders') and rfq.is_rental_orders else 'No',
                            data_style)
            rfq_sheet.write(row, 12, rfq.milestone_template_id.name if hasattr(rfq,
                                                                               'milestone_template_id') and rfq.milestone_template_id else '',
                            data_style)

            # Handle many2many fields
            analytic_groups = ''
            if hasattr(rfq, 'analytic_account_group_ids') and rfq.analytic_account_group_ids:
                analytic_groups = ', '.join([group.name for group in rfq.analytic_account_group_ids])
            rfq_sheet.write(row, 13, analytic_groups, data_style)

            rfq_sheet.write(row, 14, rfq.payment_term_id.name if rfq.payment_term_id else '', data_style)

            # Write first product line
            if lines[0]:
                rfq_sheet.write(row, 15, lines[0].product_id.name or '', data_style)
                rfq_sheet.write(row, 16, lines[0].product_uom_qty or 0.0, data_style)
                rfq_sheet.write(row, 17, lines[0].product_uom.name or '', data_style)
                rfq_sheet.write(row, 18, lines[0].price_unit or 0.0, data_style)
                taxes = ', '.join([tax.name for tax in lines[0].taxes_id]) if lines[0].taxes_id else ''
                rfq_sheet.write(row, 19, taxes, data_style)
                analytic_tags = ', '.join([tag.name for tag in lines[0].analytic_tag_ids]) if lines[
                    0].analytic_tag_ids else ''
                rfq_sheet.write(row, 20, analytic_tags, data_style)

            row += 1

            # Write additional product lines without repeating RFQ header information
            for line in lines[1:]:
                if line:
                    # Leave RFQ header columns empty for additional lines
                    rfq_sheet.write(row, 15, line.product_id.name or '', data_style)
                    rfq_sheet.write(row, 16, line.product_uom_qty or 0.0, data_style)
                    rfq_sheet.write(row, 17, line.product_uom.name or '', data_style)
                    rfq_sheet.write(row, 18, line.price_unit or 0.0, data_style)
                    taxes = ', '.join([tax.name for tax in line.taxes_id]) if line.taxes_id else ''
                    rfq_sheet.write(row, 19, taxes, data_style)
                    analytic_tags = ', '.join(
                        [tag.name for tag in line.analytic_tag_ids]) if line.analytic_tag_ids else ''
                    rfq_sheet.write(row, 20, analytic_tags, data_style)
                    row += 1

        # Finalize and return the Excel file
        name_file = 'RFQs_Export_%s' % fields.Date.today().strftime('%Y%m%d')
        workbook.close()
        xlsx_data = output.getvalue()

        response = request.make_response(
            xlsx_data,
            headers=[
                ('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
                ('Content-Disposition', 'attachment; filename=%s.xlsx' % name_file)
            ]
        )
        return response
