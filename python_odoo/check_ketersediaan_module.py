def check_list_modules_ai(self):
    module_names_to_check = [
        'Manufacturing', 'CRM Module', 'Sales Module', 'Purchase Module',
        'Construction Module', 'Inventory Module', 'HRM'
    ]
    for module_name in module_names_to_check:
        crm_module = self.env['crm.module']
        module = crm_module.search([('name', '=', module_name)])
        if not module:
            crm_module.create({'name': module_name})
            print(f"Created module: {module_name}")

            # def update_modules_ai(self):
            #     batch_size = 200
            #     offset = 0
            #     while True:
            #         leads = self.search([('modules_ids', '=', False)], limit=batch_size, offset=offset)
            #         if not leads:
            #             break
            #         for lead in leads:
            #             sale_orders = self.env['sale.order'].search([('opportunity_id', '=', lead.id),('state', '!=', 'done')])
            #             if not sale_orders:
            #                 continue
            #             descriptions = []
            #             for order in sale_orders:
            #                 for line in order.order_line:
            #                     if line.name:
            #                         descriptions.append(line.name)
            #
            #             description_text = ', '.join(descriptions) if descriptions else ""
            #             suggested_modules_dict = self.fetch_modules_from_ai(description_text)  # Fetch module names from AI
            #
            #             if suggested_modules_dict:
            #                 module_names = [module_name for module_name, value in suggested_modules_dict.items() if value == 1]  # Get module names where value is 1
            #                 module_records = self.env['crm.module'].search([('name', 'in', module_names)])
            #                 if module_records:
            #                     _logger.info('ini adalah module records',module_records)
            #                     lead.write({'modules_ids': [(6, 0, module_records.ids)]})
            #                 else:
            #                     _logger.info(f"Lead {lead.id}: No modules found with names: {module_names}")
            #             else:
            #                 _logger.info(f"Lead {lead.id}: No modules suggested by AI.")
            #
            #         offset += batch_size
            #         self._cr.commit()
