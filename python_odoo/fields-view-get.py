from odoo import models, fields, api
from lxml import etree
from json import loads as simplejson
from odoo.addons.base.models.ir.ui.view import (transfer_field_to_modifiers, transfer_node_to_modifiers, transfer_modifiers_to_node,)

def setup_modifiers(node, field=None, context=None, in_tree_view=False):
    modifiers = {}
    if field is not None:
        transfer_field_to_modifiers(field, modifiers)
    transfer_node_to_modifiers(
        node, modifiers, context=context)
    transfer_modifiers_to_node(modifiers, node)
class ResPartner(models.Model):
    _inherit = 'res.partner'

    view_get = fields.Boolean(string='View Get', default=True)



    @api.model
    def fields_view_get(self, view_id=None, view_type=False, toolbar=False, submenu=False):
        res = super().fields_view_get(view_id=view_id, view_type=view_type, toolbar=toolbar, submenu=submenu)
        doc = etree.XML(res['arch'])
        if view_type == 'form':
            for node in doc.xpath("//field"):
                modifiers = simplejson.loads(node.get('modifiers'))
                modifiers['readonly'] = [['state', '=', 'approved']]
                node.set('modifiers', simplejson.dumps(modifiers))
            node = doc.xpath("//field[@name='target_left']")[0]
            node.set('readonly', '1')
            setup_modifiers(node, res['fields']['target_left'])

            # make team leader field readonly
            team_leader_node = doc.xpath("//field[@name='team_leader_id']")[0]
            node = team_leader_node[0]
            node.set('readonly', '1')
            modifiers = simplejson.loads(node.get('modifiers'))
            modifiers['readonly'] = True
            node.set('modifiers', simplejson.dumps(modifiers))
            setup_modifiers(node, res['fields']['team_leader_id'])
        
        res['arch'] = etree.tostring(doc)
        return res



            