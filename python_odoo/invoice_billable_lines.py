for line in order.order_line:
    is_invoiceable = not float_is_zero(line.qty_to_invoice, precision_digits=precision)

    # PATCH INI: lewati pengecekan qty jika purchase_method = 'purchase'
    if not is_invoiceable and line.product_id.purchase_method == 'purchase':
        is_invoiceable = True

    if is_invoiceable:
        ...
