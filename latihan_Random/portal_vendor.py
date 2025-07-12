@http.route(['/export-purchase-orders'], type='http', auth="user", website=True)
    def export_purchase_orders(self, **post):
        """Export selected purchase orders to Excel"""
        if not post.get('ids'):
            return request.redirect('/my/rfq')
            
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet('Purchase Orders')
        
        # Get the selected purchase order IDs
        order_ids = list(map(int, post['ids'].split(',')))
        
        # Define styles
        header_style = workbook.add_format({
            'bold': True, 
            'font_size': 12,
            'align': 'center',
            'valign': 'vcenter',
            'bg_color': '#f2f2f2',
            'border': 1
        })
        
        cell_style = workbook.add_format({
            'font_size': 11,
            'align': 'left',
            'valign': 'vcenter',
            'border': 1
        })
        
        number_style = workbook.add_format({
            'font_size': 11,
            'align': 'right',
            'valign': 'vcenter',
            'border': 1,
            'num_format': '#,##0.00'
        })
        
        date_style = workbook.add_format({
            'font_size': 11,
            'align': 'center',
            'valign': 'vcenter',
            'border': 1,
            'num_format': 'yyyy-mm-dd'
        })
        
        # Set column widths
        worksheet.set_column(0, 0, 20)  # Order Reference
        worksheet.set_column(1, 1, 20)  # Tender
        worksheet.set_column(2, 2, 15)  # Order Date
        worksheet.set_column(3, 3, 15)  # Created Date
        worksheet.set_column(4, 4, 15)  # Total
        worksheet.set_column(5, 5, 15)  # Price Rating
        worksheet.set_column(6, 6, 20)  # Vendor
        worksheet.set_column(7, 7, 20)  # Company
        
        # Write headers
        headers = [
            'Order Reference', 
            'Tender', 
            'Order Date', 
            'Created Date', 
            'Total', 
            'Price Rating',
            'Vendor',
            'Company'
        ]
        
        for col, header in enumerate(headers):
            worksheet.write(0, col, header, header_style)
        
        # Get purchase orders
        PurchaseOrder = request.env['purchase.order'].sudo()
        orders = PurchaseOrder.browse(order_ids)
        
        # Apply multi-company filtering if applicable
        if len(request.env.companies) > 1:
            # Filter orders for all selected companies
            orders = orders.filtered(lambda r: r.company_id.id in request.env.companies.ids)
        else:
            # Filter orders for current company only
            orders = orders.filtered(lambda r: r.company_id.id == request.env.company.id)
        
        # Write data
        row = 1
        for order in orders:
            worksheet.write(row, 0, order.name or '', cell_style)
            worksheet.write(row, 1, order.agreement_id.name if order.agreement_id else '', cell_style)
            worksheet.write(row, 2, order.date_order, date_style)
            worksheet.write(row, 3, order.create_date, date_style)
            worksheet.write(row, 4, order.amount_total, number_style)
            worksheet.write(row, 5, order.price_rating or '', cell_style)
            worksheet.write(row, 6, order.partner_id.name or '', cell_style)
            worksheet.write(row, 7, order.company_id.name or '', cell_style)
            row += 1
            
            # Add product details in the next rows
            if order.order_line:
                # Add product headers
                product_headers = [
                    'Product',
                    'Description',
                    'Quantity',
                    'UoM',
                    'Unit Price',
                    'Taxes',
                    'Subtotal'
                ]
                
                # Indent product headers
                worksheet.write(row, 1, 'Products:', cell_style)
                row += 1
                
                for col, header in enumerate(product_headers):
                    worksheet.write(row, col + 1, header, header_style)
                row += 1
                
                # Add product lines
                for line in order.order_line:
                    worksheet.write(row, 1, line.product_id.display_name or '', cell_style)
                    worksheet.write(row, 2, line.name or '', cell_style)
                    worksheet.write(row, 3, line.product_qty, number_style)
                    worksheet.write(row, 4, line.product_uom.name if line.product_uom else '', cell_style)
                    worksheet.write(row, 5, line.price_unit, number_style)
                    worksheet.write(row, 6, ', '.join(tax.name for tax in line.taxes_id) or '', cell_style)
                    worksheet.write(row, 7, line.price_subtotal, number_style)
                    row += 1
                
                # Add a blank row after each order's products
                row += 1
        
        workbook.close()
        xlsx_data = output.getvalue()
        
        # Prepare the HTTP response with the Excel file
        response = request.make_response(
            xlsx_data,
            headers=[
                ('Content-Type', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'),
                ('Content-Disposition', 'attachment; filename=purchase_orders.xlsx;')
            ]
        )
        
        return responsea