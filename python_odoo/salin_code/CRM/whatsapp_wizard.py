from odoo import api, fields, models
import html2text

class WhatsappSendMessage(models.TransientModel):
    _inherit = 'whatsapp.message.wizard'

    crm_lead = fields.Boolean('CRM Lead')
    company_name = fields.Char('Company Name')

    def send_message(self):
        number = self._context.get('default_mobile_number', False)
        if number:
            self.mobile_number = number
        if self.message and self.mobile_number:
            message_string = ''
            message = self.message.split(' ')
            for msg in message:
                message_string = message_string + msg + '%20'
            message_string = message_string[:(len(message_string) - 3)]
            number = self.mobile_number
            link = "https://web.whatsapp.com/send?phone=" + number
            send_msg = {
                'type': 'ir.actions.act_url',
                'target': 'new',
                'url': link + '&text=' + message_string,
                'res_id': self.id
            }
            return send_msg