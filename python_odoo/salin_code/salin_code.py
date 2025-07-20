from odoo import models, fields, api, _

class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    @api.depends('brand_id')
    def _compute_display_name(self):
        for vehicle in self:
            name = vehicle.name
            if vehicle.brand_id.name:
                name = f"{vehicle.brand_id.name} {name}"
            vehicle.display_name = name

    @api.depends('range_unit')
    def _compute_co2_emission_unit(self):
        for record in self:
            if record.range_unit == 'km':
                record.co2_emission_unit = 'kg/km'
            else:
                record.co2_emission_unit = 'kg/l'

    def action_model_vehicle(self):
        self.ensure_one()
        context = {'default_vehicle_id': self.id}
        if self.vehicle_count:
            view_mode = 'tree,form,kanban'
            name = _('Vehicles')
            context['search_default_model_id'] = self.id
        else:
            view_mode = 'form'
            name = _('New Vehicle')
        view = {
            'type': 'ir.actions.act_window',
            'name': name,
            'view_mode': view_mode,
            'res_model': 'fleet.vehicle',
            'context': context,
            'target': 'new',
        }
        return view

    def _compute_vehicle_count(self):
        group = self.env['fleet.vehicle']._read_group(
            [('model_id', 'in', self.ids)],
            ['model_id'],
            aggregates = ['__count']
        )
        count_by_model = {model.id: count for model, count in group}
        for model in self:
            model.vehicle_count = count_by_model.get(model.id, 0)
