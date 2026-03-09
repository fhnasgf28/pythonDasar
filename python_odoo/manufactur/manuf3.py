def action_confirm(self):
    if self.env.context.get('do_not_confirm_production', False):
        return

    for production in self:
        for workorder in production.workorder_ids:
            print('workorder codingn ini di eksekusi tau gaes')
            workorder._hide_buttons_workorder_line()
        production._check_product_cost_method()
        if production.sale_order_id or (production.mrp_plan_id and production.mrp_plan_id.sale_order_id):
            workorder_ids = production.workorder_ids.filtered(lambda wo: wo.state in ['ready', 'pending'])
            workorder_ids.leave_id.unlink()

    res = super(MrpProduction, self).action_confirm()
