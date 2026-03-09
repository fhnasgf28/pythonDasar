def button_confirm(self):
    for record in self:
        if record.consumption == 'warning':
            production = record.env['mrp.production'].search([('bom_id', '=', record.id)], limit=1)
            if production:
                material_status = production.reservation_state  # Bisa 'assigned', 'partially_available', atau 'not_available'

                if material_status in ['not_available', 'partially_available']:
                    raise UserError(
                        "Warning: Material is not fully available! Please check before confirming the work order.")
    self.ensure_one()