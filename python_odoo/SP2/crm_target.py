import simplejson
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError, _
from odoo.tools import html2plaintext
from xml import etree
from odoo.addons.base.models.ir_ui_view import (transfer_field_to_modifiers, transfer_node_to_modifiers,transfer_modifiers_to_node)

def setup_modifiers(node, field=None, context=None, in_tree_view=False):
    modifiers = {}
    if field is not None:
        transfer_field_to_modifiers(field, modifiers)
    transfer_node_to_modifiers(node, modifiers,context=context)
    transfer_modifiers_to_node(modifiers,node)

def make_field_readonly(doc, field_name, res):
    nodes = doc.xpath("//field[@name='%s']" % field_name)
    if nodes:
        node = nodes[0]
        node.set('readonly', '1')
        modifier = simplejson.loads(node.get('modifiers') or '{}')
        modifier['readonly'] = True
        node.set('modifiers', simplejson.dumps(modifier))
        setup_modifiers(node,res['fields'][field_name])

class CrmTarget(models.Model):
    _inherit = 'crm.target'

    @api.depends('state', 'salesperson_id', 'team_leader_id')
    def _compute_hide(self):
        for rec in self:
            hide_button = True
            current_user = self.env.user
            if rec.state == 'draft':
                if rec.salesperson_id.id or rec.team_leader_id.id:
                    hide_button = False
            elif rec.state == 'waiting_approval':
                is_leader = False
                if rec.team_leader_id.user_id or current_user.id:
                    is_leader = True
                if rec.sale_team_id.additional_leader_ids.ids or current_user.id:
                    is_leader = True
                if is_leader:
                    hide_button = False

            elif rec.state == 'rejected':
                rejected_button = False
                if rec.salesperson_id.id and rec.team_leader_id.id or current_user.id:
                    rejected_button = True
                if rec.sale_team_id.additional_leader_ids.ids or current_user.id:
                    rejected_button = True
                if rec.sale_team_id.user_id or current_user.id:
                    rejected_button = True
                if rejected_button:
                    hide_button = False
            rec.hide = hide_button


    def get_team_members_and_leaders(self):
        """
        Get team members and team leaders based on sale_team_id.
        """
        self.ensure_one()

        team = self.sale_team_id
        if not team:
            return {
                'team_members': self.env['res.users'],
                'team_leaders': self.env['res.users'],
                'all_users': self.env['res.users']
            }

        # Get all team members
        team_members = team.member_ids

        # Get all leaders
        team_leaders = self.env['res.users']
        if team.user_id:
            team_leaders |= team.user_id
        if team.additional_leader_ids:
            team_leaders |= team.additional_leader_ids

        # Combine members + leaders
        all_users = team_members | team_leaders

        return {
            'team_members': team_members,
            'team_leaders': team_leaders,
            'all_users': all_users
        }

    def print_team_access_info(self):
        """
        Prints detailed information about team members and leaders.
        Useful for debugging and verification.
        """
        self.ensure_one()
        access_info = self.get_team_members_and_leaders()

        print("\n=== Team Access Information ===")
        print(f"Team: {self.name} (ID: {self.id})")

        print("\nTeam Members:")
        for member in access_info['team_members']:
            print(f"- {member.name} (ID: {member.id})")

        print("\nTeam Leaders:")
        for leader in access_info['team_leaders']:
            print(f"- {leader.name} (ID: {leader.id})")

        print("\nAll Users with Access:")
        for user in access_info['all_users']:
            print(f"- {user.name} (ID: {user.id})")

        return True

    def check_date(self, start_date, end_date, based_on):
        for rec in self:
            overlapping_targets = self.env['crm.target'].search([
                ('id', '!=', rec.id),
                ('salesperson_id', '=', rec.salesperson_id.id),
                ('based_on', '=', based_on),
                ('state', '!=', 'rejected'),
                '|', '|',
                '&', ('start_date', '<=', start_date), ('end_date', '>=', start_date),
                '&', ('start_date', '<=', end_date), ('end_date', '>=', end_date),
                '&', ('start_date', '>=', start_date), ('end_date', '<=', end_date),
            ])

            if overlapping_targets:
                raise ValidationError("You already have a target for this period.")

    def button_approve(self):
        for rec in self:
            current_user = self.env.user
            if rec.team_leader_id.id:
                rec.state = 'approved'
            else:
                raise ValidationError(_("Only the team leader can approve this target."))

    def button_reject(self):
        for rec in self:
            current_user = self.env.user
            if rec.team_leader_id.id:
                rec.state = 'rejected'
            else:
                raise ValidationError(_("Only the team leader can reject this target."))

    @api.depends('sale_team_id', 'company_id')
    def _compute_available_salesperson_ids(self):
        user = self.env['res.users']
        company_id = self.env.company.id
        for rec in self:
            sales_team = self.env['crm.team'].search([
                '|',
                ('company_id', '=', company_id),
                ('company_id', '=', False),
            ])
            # get all members from all sales teams
            all_team_members = user.browse()
            for sales_team in sales_team:
                all_team_members |= sales_team.member_ids
            rec.available_salesperson_ids = all_team_members
            if rec.sale_team_id:
                rec.available_salesperson_ids = rec.sale_team_id.member_ids

    @api.onchange('salesperson_id')
    def _onchange_salesperson_id(self):
        for rec in self:
            if rec.salesperson_id:
                team = self.env['crm.team'].search([
                    ('member_ids', 'in', rec.salesperson_id.id),
                    '|',
                    ('company_id', '=', rec.company_id.id),
                    ('company_id', '=', False),
                ])
#                 mengetahui team dengan print
                print("team",team)
                if team:
                    rec.sale_team_id = team[0].id

    @api.model
    def fields_view_get(self, view_id=None, view_type=False, toolbar=False, submenu=False):
        res = super().fields_view_get(view_id=view_id, view_type=view_type,toolbar=toolbar,submenu=submenu)
        doc = etree.XML(res['arch'])
        if view_type == 'form':
            for node in doc.xpath('//field'):
                node.set('readonly', '1')
        setup_modifiers(node, res['fields']['target_left'])
        make_field_readonly(doc, 'company_id', res)
        make_field_readonly(doc, 'salesperson_id', res)
        return res





