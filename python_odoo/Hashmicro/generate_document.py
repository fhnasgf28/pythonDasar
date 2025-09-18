from odoo import models, fields, api
import base64

class GenerateDocument(models.Model):
    _inherit = 'sale.order'

    def _generate_document_pdf_for_po(self, purchase_order):
        # logic generate PDF untuk PO
        report = self.env.ref('purchase.action_report_purchase_order')
        pdf_content, _ = report._render_qweb_pdf(purchase_order.id)
        return self.env['ir.attachment'].create({
            'name': purchase_order.name + '.pdf',
            'res_model': purchase_order._name,
            'res_id': purchase_order.id,
            'type': 'binary',
            'mimetype': 'application/pdf',
            'datas': base64.b64encode(pdf_content),
        })
