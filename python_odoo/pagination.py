class CustomerPortal(CustomerPortal):
    @http.route(['/my/quotes', '/my/quotes/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_quotes(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):
        values = self._prepare_portal_layout_values()
        partner = requests.env.user.partner_id
        SaleOrder = request.env.['sale.order']
        if requests.env.user.has_group('base.group_portal'):
            domain = [
                ('state', 'in', ['sent', 'cancel']),
                ('partner_id', '=', partner.id)]
            else:
            domain = [
                ('message_partner_ids', 'child_of',
                 [partner.commercial_partner_id.id]),
                ('state', 'in', ['sent', 'cancel'])]
        searchbar_sortings = {
            'date': {'label': _('Order Date'), 'order': 'date_order desc'},
            'name': {'label': _('Reference'), 'order': 'name'},
            'stage': {'label': _('Stage'), 'order': 'state'},
        }
        if not sortby:
            sortby = 'date'
        sort_order = searchbar_sortings[sortby]['order']
        quotation_count = SaleOrder.search_count(domain)
        pager = portal_pager(
            url="/my/quotes",
            url_args={'date_begin': date_begin, 'date_end': date_end,
                      'sortby': sortby},
            total=quotation_count,
            page=page,
            step=15
        )
        # search the count to display, according to the pager data
        quotations = SaleOrder.search(domain, order=sort_order,
                                      limit=15,
                                      offset=pager['offset'])
        request.session['my_quotations_history'] = quotations.ids[:100]
        values.update({
            'date': date_begin,
            'quotations': quotations.sudo(),
            'page_name': 'quote',
            'pager': pager,
            'default_url': '/my/quotes',
            'searchbar_sortings': searchbar_sortings,
            'sortby': sortby,
        })
        return request.render("sale.portal_my_quotations", values)
            ]