def _hide_buttons_workorder_line(self):
    for workorder in self:
        if workorder.production_id.bom_id:
            workorder.hide_buttons = workorder.production_id.bom_id.consumption == 'strict'
            print('workorder.hide_buttons', workorder.hide_buttons)


def create_consumption(self, confirm_and_assign=False):
    consumption = self.env['mrp.consumption'].create(self._prepare_consumption_vals())
    if not confirm_and_assign:
        return consumption
    draft_moves = (consumption.move_raw_ids | consumption.byproduct_ids | consumption.move_finished_ids).filtered(
        lambda m: m.state == 'draft')
    draft_moves._action_confirm()

    confirmed_move_raws = consumption.move_raw_ids.filtered(lambda m: m.state == 'confirmed')
    if confirmed_move_raws:
        confirmed_move_raws._action_assign()

    for move in consumption.move_raw_ids | consumption.byproduct_ids | consumption.move_finished_ids:
        if (move.production_id and move.state == 'confirmed') or (
                move.raw_material_production_id and move.state == 'assigned'):
            move.mrp_quantity_done = move.product_uom_qty
            if move.raw_material_production_id:
                for move_line in move.move_line_ids:
                    move_line.qty_done = move_line.product_uom_qty
    return consumption