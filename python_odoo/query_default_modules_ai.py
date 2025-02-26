def update_modules_ai(self):
    batch_size = 200
    offset = 0
    cr = self._cr
    while True:
        leads = self.search([('modules_ids', '=', False)], limit=batch_size, offset=offset)
        if not leads:
            break

        lead_ids = tuple(leads.ids)
        if not lead_ids:
            break

        # Query langsung ke database untuk mendapatkan sale orders
        cr.execute("""
                SELECT so.id, so.opportunity_id
                FROM sale_order so
                WHERE so.opportunity_id IN %s 
                AND so.state != 'done'
                AND so.modules_ai_processed = FALSE
            """, (lead_ids,))

        sale_orders = cr.fetchall()  # [(id, opportunity_id), ...]

        if not sale_orders:
            offset += batch_size
            continue

        # Mapping opportunity_id ke sale_order_id
        sale_order_map = {}
        sale_order_ids = []
        for sale_order_id, opportunity_id in sale_orders:
            sale_order_map.setdefault(opportunity_id, []).append(sale_order_id)
            sale_order_ids.append(sale_order_id)

        if not sale_order_ids:
            offset += batch_size
            continue

        # Query untuk mengambil order_line.name berdasarkan sale_order_id
        cr.execute("""
                SELECT sol.name, so.opportunity_id
                FROM sale_order_line sol
                JOIN sale_order so ON sol.order_id = so.id
                WHERE so.id IN %s
            """, (tuple(sale_order_ids),))

        order_lines = cr.fetchall()  # [(name, opportunity_id), ...]

        # Mapping opportunity_id ke order descriptions
        descriptions_map = {}
        for line_name, opportunity_id in order_lines:
            if line_name:
                descriptions_map.setdefault(opportunity_id, []).append(line_name)

        for lead in leads:
            opportunity_id = lead.id
            descriptions = descriptions_map.get(opportunity_id, [])
            description_text = ', '.join(descriptions) if descriptions else ""

            suggested_modules = self.fetch_modules_from_ai(description_text)  # Fetch module names from AI

            if suggested_modules:
                suggested_modules_dict = json.loads(suggested_modules)
                module_names = [module_name for module_name, value in suggested_modules_dict.items() if value == 1]

                if module_names:
                    # Query sekali untuk mencari semua module yang diperlukan
                    module_records = self.env['crm.module'].search([('name', 'in', module_names)])

                    if module_records:
                        lead.write({'modules_ids': [(6, 0, module_records.ids)]})

                        # Update sale.order untuk menandai `modules_ai_processed`
                        cr.execute("""
                                UPDATE sale_order 
                                SET modules_ai_processed = TRUE 
                                WHERE id IN %s
                            """, (tuple(sale_order_map.get(opportunity_id, [])),))
                    else:
                        _logger.info(f"Lead {lead.id}: No modules found with names: {module_names}")
                else:
                    _logger.info(f"Lead {lead.id}: No modules suggested by AI.")

        offset += batch_size
        cr.commit()
    return True
