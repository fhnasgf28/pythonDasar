    def action_view_sale_quotation(self):
        self.check_hold()
        res = self.env.ref('sale.action_quotations_with_onboarding').read()[0]
        
        # Safely evaluate context string into a dictionary
        context = safe_eval(res.get('context', '{}'))
        
        # Remove default filter
        if 'search_default_draft' in context:
            del context['search_default_draft']
        if self.type == 'opportunity':
            context['create'] = False
        
        # Update res with the modified context and domain
        res['context'] = context
        res['domain'] = [('opportunity_id', '=', self.id), ('state', 'not in', ['sale', 'done'])]
    
        # Force the custom tree view
        try:
            tree_view_id = self.env.ref('equip3_sale_operation.view_sale_order_quotation_tree_custom').id
            res['views'] = [(tree_view_id, 'tree'), (False, 'form')]
            res['view_mode'] = 'tree,form'
        except ValueError:
            pass
        
        return res