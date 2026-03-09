# -*- coding: utf-8 -*-

# from turtle import pos

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class GeneratePosVoucherWizard(models.TransientModel):
    _name = 'generate.pos.voucher.wizard'
    _description = 'Generate Pos Voucher Wizard'

    no_of_voucher = fields.Integer('No Of Vouchers', default=1, )
    amount_of_usage = fields.Integer('Amount Of Usage', default=1,
                                     help='The number of each vouchers usage, if 0 = unlimited')
    voucher_template_id = fields.Many2one('generate.pos.voucher', 'Voucher Template')

    def action_confirm(self):
        new_vouchers = self.env['pos.voucher']
        template = self.voucher_template_id
        voucher_ids = []
        for count in range(0, self.no_of_voucher):
            values = {
                'is_generate_voucher': True,
                'generated_source_id': template.id,
                'source_document_id': template.id,

                'start_date': template.start_date,
                'method': template.method,
                'minimum_purchase_amount': template.minimum_purchase_amount,
                'maximum_discount_amount': template.maximum_discount_amount,
                'state': template.state,
                'use_date': template.use_date,
                'receipt_template_id': self.env.context.get('receipt_template_id'),
                'end_date': template.end_date,
                'apply_type': template.apply_type,
                'value': template.value,
                'source': template.source,
                'limit_restrict_product_ids': template.limit_restrict_product_ids,
                'pos_category_ids': template.pos_category_ids,
                'is_customize_sequence': template.is_customize_sequence,
                'sequence_generate_method': template.sequence_generate_method,
                'manual_input_sequence': template.manual_input_sequence,
                'running_number_prefix': template.running_number_prefix,
                'running_number_digit': template.running_number_digit,

                'no_of_usage': self.amount_of_usage,
            }

            if template.user_id:
                values['user_id'] = template.user_id.id
            if template.brand_ids:
                values['brand_ids'] = [(6, 0, template.brand_ids.ids)]
            if template.company_ids:
                values['company_ids'] = [(6, 0, template.company_ids.ids)]

            voucher = self.env['pos.voucher'].create(values)
            voucher_ids += [voucher.id]

        return {
            'name': _('Vouchers'),
            'view_mode': 'tree,form',
            'res_model': 'pos.voucher',
            'type': 'ir.actions.act_window',
            'domain': [('id', 'in', voucher_ids)],
            'context': {}
        }