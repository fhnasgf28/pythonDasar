# -*- coding: utf-8 -*-

from odoo import fields, models


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    x_ktt_leads2_id = fields.Char(index=True, copy=False)
