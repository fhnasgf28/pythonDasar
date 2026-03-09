from odoo import fields, models, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    def _get_available_resource_types(self):
        # Mendapatkan semua resource types yang tersedia
        resource_types = self.env['business.resource.type'].search([])
        return [(str(rt.id), rt.name) for rt in resource_types]

    def _get_available_resources(self):
        # Mendapatkan semua resources yang tersedia
        resources = self.env['business.resource'].search([])
        return [(str(r.id), r.name) for r in resources]

    def _get_available_services(self):
        # Mendapatkan semua services yang tersedia
        services = self.env['appointment.product'].search(
            [('is_appointment_service', '=', True)])  # Sesuaikan dengan domain yang kamu gunakan
        return [(str(s.id), s.name) for s in services]

    resource_type_id = fields.Selection(
        selection='_get_available_resource_types',
        string='Default Resource Type for Appointments',
        config_parameter='business_appointment.default_resource_type_id'
    )
    resource_ids = fields.Selection(
        selection='_get_available_resources',
        string='Available Resources for Appointments',
        config_parameter='business_appointment.available_resource_ids'
    )
    service_ids = fields.Selection(
        selection='_get_available_services',
        string='Available Services for Appointments',
        config_parameter='business_appointment.available_service_ids'
    )

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res.update(
            resource_type_id=self.env['ir.config_parameter'].sudo().get_param(
                'business_appointment.default_resource_type_id'),
            resource_ids=self.env['ir.config_parameter'].sudo().get_param(
                'business_appointment.available_resource_ids'),
            service_ids=self.env['ir.config_parameter'].sudo().get_param(
                'business_appointment.available_service_ids'),
        )
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('business_appointment.default_resource_type_id',
                                                         self.resource_type_id)
        self.env['ir.config_parameter'].sudo().set_param('business_appointment.available_resource_ids',
                                                         self.resource_ids)
        self.env['ir.config_parameter'].sudo().set_param('business_appointment.available_service_ids',
                                                         self.service_ids)
