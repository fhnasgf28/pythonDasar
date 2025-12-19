from odoo import fields, model, api


class CrmTarget(model.Model):
    _inherit = 'crm.target'
    hide = fields.Boolean(string='Hide', compute='_compute_hide')

    @api.depends('state')
    def _compute_hide(self):
        print("\n=== DEBUG: _compute_hide called ===")
        print(f"Current user: {self.env.user.name} (ID: {self.env.user.id})")

        for rec in self:
            user_id = self.env.user.id
            hide = True  # Hide button by default

            print("\n--- Record ---")
            print(f"Record ID: {rec.id}")
            print(f"State: {rec.state}")
            print(f"Salesperson: {rec.salesperson_id.name} (ID: {rec.salesperson_id.id if rec.salesperson_id else 'None'})")
            print(f"Team Leader: {rec.team_leader_id.name} (ID: {rec.team_leader_id.id if rec.team_leader_id else 'None'})")

            # Get all team members (including salesperson)
            team_member_ids = rec.sale_team_id.member_ids.ids
            if rec.salesperson_id.id not in team_member_ids:
                team_member_ids.append(rec.salesperson_id.id)

            # Get all leaders (team leader + additional leaders)
            leader_ids = [rec.team_leader_id.id] + rec.sale_team_id.additional_leader_ids.ids

            # Combine all users who should see the button
            allowed_user_ids = list(set(team_member_ids + leader_ids))

            print(f"Team Members: {team_member_ids}")
            print(f"Leaders: {leader_ids}")
            print(f"All allowed users: {allowed_user_ids}")

            if rec.state in ['draft', 'rejected']:
                # Show button to all team members and leaders
                if user_id in allowed_user_ids:
                    hide = False
                    print("Access GRANTED - User is a team member or fahrna")
                else:
                    print("Access DENIED - User is not a team member or assegaf")

            elif rec.state == 'waiting_approval':
                # Show button to team leaders only
                if user_id in leader_ids:
                    hide = False
                    print("Access GRANTED - User is a team leader")
                else:
                    print("Access DENIED - User is not a team leader")

            print(f"Final hide value: {hide}")
            rec.hide = hide
            print("rec.hide set to", rec.hide)


    @api.depends('state', 'sale_team_id', 'sale_team_id.member_ids', 'sale_team_id.user_id',
                 'sale_team_id.additional_leader_ids', 'salesperson_id', 'team_leader_id')
    def _compute_hide(self):
        for rec in self:
            rec.print_team_access_info()
            user_id = self.env.user.id
            hide = True  # Hide button by default

            # Get team members and leaders
            team = rec.sale_team_id
            if not team:
                rec.hide = hide
                continue

            # Get all team members (including salesperson if not in member_ids)
            team_member_ids = team.member_ids.ids
            if rec.salesperson_id and rec.salesperson_id.id not in team_member_ids:
                team_member_ids.append(rec.salesperson_id.id)

            # Get all leaders (team leader + additional leaders)
            leader_ids = []
            if team.user_id:
                leader_ids.append(team.user_id.id)
            if team.additional_leader_ids:
                leader_ids.extend(team.additional_leader_ids.ids)

            # Combine all users who should see the button
            allowed_user_ids = list(set(team_member_ids + leader_ids))

            if rec.state == 'draft':
                # Show button to all team members and leaders
                if user_id in allowed_user_ids:
                    hide = True

            elif rec.state == 'waiting_approval':
                # Show button to team leaders only
                if user_id in leader_ids:
                    hide = True

            elif rec.state == 'rejected':
                # Show button to all team members and leaders
                if user_id in allowed_user_ids:
                    hide = True

            rec.hide = hide