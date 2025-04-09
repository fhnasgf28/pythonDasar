def _pre_button_confirm(self, check_default=True, do_check_consumption=True):
    self.ensure_one()

    if check_default:
        rounding = self.env['decimal.precision'].precision_get('Product Unit of Measure')

        if self.is_last_workorder:

            # check fg tracking
            tracking_finished = self.move_finished_ids.filtered(lambda b: b.product_id.tracking in ('lot', 'serial'))
            for product_id in tracking_finished.mapped('product_id'):
                to_generate_qty = 0.0
                for move in tracking_finished.filtered(lambda b: b.product_id == product_id):
                    qty = move.mrp_quantity_done
                    if move.has_tracking == 'serial':
                        qty = move.product_uom._compute_quantity(qty, move.product_id.uom_id)
                    to_generate_qty += qty
                generated_qty = sum(
                    self.finished_lot_ids.filtered(lambda l: l.product_id == product_id).mapped('consumption_qty'))

                if float_compare(to_generate_qty, generated_qty, precision_digits=rounding) != 0:
                    err_message = _(
                        'The amount of generated lot/serial number for finished product is not the same as produced quantity!\nGenerate/delete some lot/serial number first!')
                    return err_message, False

            # check rejected tracking
            rejected_product = self.manufacturing_order_id.bom_rejected_product_id
            if rejected_product.tracking in ('lot', 'serial'):
                to_generate_qty = self.rejected_qty
                if rejected_product.tracking == 'serial':
                    to_generate_qty = self.product_uom_id._compute_quantity(to_generate_qty, rejected_product.uom_id)
                generated_qty = sum(self.rejected_lot_ids.mapped('consumption_qty'))

                if float_compare(to_generate_qty, generated_qty, precision_digits=rounding) != 0:
                    err_message = _(
                        'The amount of generated lot/serial number for rejected product is not the same as produced quantity!\nGenerate/delete some lot/serial number first!')
                    return err_message, False

        partially_moves = self.move_raw_ids.filtered(lambda move: move.state == 'confirmed')
        print('partially_moves', partially_moves)
        if partially_moves:
            raise UserError(_(
                "Cannot confirm because there is still material with 'Partially Available' status."
            ))

        # check material tracking