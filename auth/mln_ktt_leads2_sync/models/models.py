# -*- coding: utf-8 -*-

from odoo import fields, models


class MlnSyncLog(models.Model):
    _name = 'mln.sync.log'
    _description = 'MLN KTT Sync Log'
    _order = 'id desc'

    ktt_leads2_id = fields.Char(index=True)
    url = fields.Char(required=True)
    payload_json = fields.Text()
    status_code = fields.Integer()
    response_text = fields.Text()
    error = fields.Text()

    sale_order_id = fields.Many2one('sale.order', ondelete='set null')
    lead_id = fields.Many2one('crm.lead', ondelete='set null')
    missing_users_json = fields.Text()
    missing_team_value = fields.Char()
    matched_domain = fields.Char()
    mapped_team = fields.Char()
    mapped_users_json = fields.Text()
    write_result = fields.Boolean()
