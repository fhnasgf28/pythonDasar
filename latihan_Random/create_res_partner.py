from odoo import models, fields, api
class ResPartner(models.Model):
    _inherit = 'res.partner'    

    @api.model
    def create(self, values):
        self.env.context = dict(self.env.context)
        
        # Ambil setting approval matrix di awal untuk konsistensi
        is_approval_matrix = False
        try:
            is_approval_matrix = self.env.ref('equip3_crm_operation.crm_setting_1').is_customer_approval_matrix
            print("Customer approval matrix setting: %s", is_approval_matrix)
        except Exception as e:
            print("Error getting approval matrix setting: %s", e)
        
        if 'is_leads' in values:
            if values.get('is_leads', False):
                sequence = self.env['ir.sequence'].next_by_code('res.partner.lead.sequence')
                values.update({
                    'lead_sequence': sequence,
                    # 'customer_rank': 0,
                    # 'customer_sequence': None,
                })
                
                # Jika customer_rank > 0 dan approval matrix dinonaktifkan, set state ke approved
                if not is_approval_matrix and values.get('customer_rank', 0) > 0:
                    values['state_customer'] = 'approved'
                    print("Setting state_customer to approved during create: %s", values.get('state_customer'))
                # Jika approval matrix aktif, pastikan state_customer adalah draft
                elif is_approval_matrix and values.get('customer_rank', 0) > 0:
                    values['state_customer'] = 'draft'
                    print("Setting state_customer to draft during create: %s", values.get('state_customer'))
                    
        if 'is_company' in values and 'create_company' in self.env.context:
            values['company_id'] = False
            
        res = super(ResPartner, self).create(values)
        
        # Double check setelah create untuk memastikan state_customer konsisten
        if 'customer_rank' in values and values.get('customer_rank', 0) > 0:
            current_state = res.state_customer
            print("Current state after create: %s, is_approval_matrix: %s", current_state, is_approval_matrix)
            
            # Jika approval matrix dinonaktifkan, pastikan state adalah approved
            if not is_approval_matrix and current_state != 'approved':
                res.write({'state_customer': 'approved'})
                print("Updated state_customer to approved after create")
            # Jika approval matrix aktif, pastikan state adalah draft (kecuali jika sudah diubah ke state lain)
            elif is_approval_matrix and current_state not in ['draft', 'waiting_approval', 'approved', 'rejected']:
                res.write({'state_customer': 'draft'})
                print("Updated state_customer to draft after create")
                
        if 'create_company' in self.env.context:
            self.env.context.update({
                'partner_id': res.id,
            })
        return res