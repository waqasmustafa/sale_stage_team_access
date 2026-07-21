# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def write(self, vals):
        # 'stage_id' below must match the technical field name on
        # sale.order that stores your custom Kanban stage. Change it
        # here if your field name is different.
        if 'stage_id' in vals and vals.get('stage_id'):
            self._check_stage_team_access(vals['stage_id'])
        return super(SaleOrder, self).write(vals)

    def _check_stage_team_access(self, new_stage_id):
        """Raise a UserError if the current user is not allowed to move
        this order into the requested stage.
        """
        user = self.env.user

        # 1. Superuser / technical calls (e.g. automations, scripts) are
        #    never restricted.
        if self.env.su:
            return

        # 2. Real Odoo System Administrators always have full access.
        if user.has_group('base.group_system'):
            return

        teams = user.team_ids

        # 3. No team assigned at all -> block, with a clear message.
        if not teams:
            raise UserError(_(
                "You are not assigned to any Team, so you are not "
                "allowed to change the Sale Order stage. Please contact "
                "your administrator."
            ))

        # 4. If any of the user's teams is the 'Admin' (full access)
        #    team, allow any stage.
        if any(team.is_admin_team for team in teams):
            return

        # 5. Otherwise, the new stage must be within the combined list
        #    of allowed stages for all of the user's teams.
        allowed_stage_ids = teams.mapped('stage_ids').ids
        if new_stage_id not in allowed_stage_ids:
            stage = self.env['sale.order.stage'].browse(new_stage_id)
            team_names = ', '.join(teams.mapped('name'))
            raise UserError(_(
                "You are not allowed to move this order to the '%(stage)s' "
                "stage.\n\nYour Team(s): %(teams)s\n"
                "Please contact your administrator if you believe this "
                "is a mistake."
            ) % {
                'stage': stage.name,
                'teams': team_names,
            })
