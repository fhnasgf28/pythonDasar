from odoo import http, fields
from odoo.http import requests
import io
import xlsxwriter

class rfq_export(http.Controller):
    @http.route(['/my/rfq/export'], type='http', auth='user', website=True, csrf=True)
    def export_selected_rfqs(self, **post):
        """export selected rfq to excel"""
        rfq_ids = []
        if post.get('selected_rfq_ids'):
            rfq_ids = [int(id) for id in post.get('selected_rfq_ids').split(',') if id]