from odoo import models, fields, api
from odoo import tools

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def _get_street(self, partner):
        print('farhan kodingan ini dieksekusi')
        res = super()._get_street(partner)
        if self.env.context.get('is_company'):
            address_from_branch_po = self.env.ref('equip3_purchase_accessright_setting.purchase_setting_1').is_enable_branch_printout_po
            address_from_branch_pr = self.env.ref('equip3_purchase_accessright_setting.purchase_setting_1').is_enable_branch_printout_pr

            if address_from_branch_po:
                print(f'kondisi PO: {address_from_branch_po}')
                res = self._prepare_address(self.branch_id)
            elif address_from_branch_pr:
                res = self._prepare_address(self.branch_id)
            else:
                res = self._prepare_address(self.company_id.partner_id)

        return res

    def _prepare_address(self, partner):
        address = ''
        if partner.street:
            address = "%s" % partner.street
        # if partner.street_2:
        #     address += ", %s" % partner.street_2

        html_text = str(tools.plaintext2html(address, container_tag=True))
        data = html_text.split('p>')

        if data:
            return data[1][:-2]
        return ''

    def _get_address_details(self, partner):
        print(f"kodingan ini dijalankan")
        res = super()._get_address_details(partner)
        if self.env.context.get('is_company'):
            address_from_branch_po = self.env.ref('equip3_purchase_accessright_setting.purchase_setting_1').is_enable_branch_printout_po
            address_from_branch_pr = self.env.ref('equip3_purchase_accessright_setting.purchase_setting_1').is_enable_branch_printout_pr

            if address_from_branch_po:
                res = self._prepare_address_details(self.branch_id)
            elif address_from_branch_pr:
                res = self._prepare_address_details(self.branch_id)
            else:
                res = self._prepare_address_details(self.company_id.partner_id)

        return res

    def _prepare_address_details(self, partner):
        address = ''
        if partner.city:
            address = "%s" % partner.city
        if partner.state_id.name:
            address += ", %s" % partner.state_id.name
        # if partner.zip_code:
        #     address += ", %s" % (partner.zip_code)
        if partner.country_id.name:
            address += ", %s" % partner.country_id.name
        html_text = str(tools.plaintext2html(address, container_tag=True))
        data = html_text.split('p>')
        if data:
            return data[1][:-2]
        return ''