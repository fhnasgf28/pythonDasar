@http.route(['/open_tender/<int:tender_id>', '/open_tender/<int:tender_id>/page/<int:page>'], type='http', auth="public",
            website=True)
def portal_open_tender_form(self, tender_id, page=1, report_type=None, access_token=None, message=False,
                            download=False, tender_dashboard_selection=False, **kw):
    if tender_dashboard_selection == 'False':
        tender_dashboard_selection = False
    tender_sudo = request.env['purchase.agreement'].sudo().search(
        [('id', '=', tender_id)], limit=1)
    if not tender_sudo:
        return request.not_found()

    if page < 1:
        page = 1

    line_field = tender_sudo.sh_purchase_agreement_line_ids
    line_count = len(line_field)
    items_per_page = self._items_per_page

    # Validate offset
    offset = (page - 1) * items_per_page
    if offset >= line_count and line_count > 0:
        return request.redirect(f"/open_tender/{tender_id}/page/1")

    pager = portal_pager(
        url=f"/open_tender/{tender_id}",
        total=line_count,
        page=page,
        step=items_per_page,
    )
    tender_lines = request.env['purchase.agreement.line'].sudo().search(
        [('agreement_id', '=', tender_sudo.id)],
        limit=items_per_page,
        offset=offset
    )
    rfq_order = request.env['purchase.order'].sudo().search(
        [('agreement_id', '=', tender_sudo.id), ('state', '!=', 'cancel')])
    purchase_order = request.env['purchase.order'].sudo().search(
        [('agreement_id', '=', tender_sudo.id), ('state', '=', 'purchase')])
    user_type = 'public'
    if request.env.user == request.env.ref('base.public_user'):
        user_type = 'public'
    else:
        if request.env.user.partner_id.is_vendor:
            user_type = 'is_vendor'
        else:
            user_type = 'bukan_vendor'
    values = {
        'token': access_token,
        'open_tender': tender_sudo,
        'message': message,
        'bootstrap_formatting': True,
        'partner_id': tender_sudo.partner_id.id,
        'report_type': 'html',
        'page_name': 'open_tender',
        'number_of_participants': len(rfq_order.mapped('partner_id')),
        'participants': rfq_order,
        'winners': purchase_order,
        'tender_dashboard_selection': tender_dashboard_selection,
        'user_type': user_type,
        'pager': pager,
        'line_fields': tender_lines,
        'default_url': f"/open_tender/{tender_id}",
        'purchase_order_id': next((purchase for purchase in tender_sudo.purchase_order_ids if purchase.partner_id == request.env.user.partner_id), False)
    }
    return request.render('equip3_purchase_vendor_portal.portal_open_tender_form_template', values)
