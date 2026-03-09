from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    resource_type = fields.Selection(
        selection=[
            ('human', 'Human Resource'),
            ('material', 'Material Resource'),
            ('virtual', 'Virtual Resource'),
        ],
        string='Default Resource Type for Appointments'
    )
    resource = fields.Selection(
        selection=[
            ('manager', 'Manager'),
            ('staff', 'Staff'),
            ('consultant', 'Consultant'),
        ],
        string='Available Resources for Appointments'
    )
    service = fields.Selection(
        selection=[
            ('meeting', 'Meeting'),
            ('training', 'Training'),
            ('consultation', 'Consultation'),
        ],
        string='Available Services for Appointments'
    )
