# -*- coding: utf-8 -*-
from odoo import models, fields


class ResUsers(models.Model):
    _inherit = 'res.users'

    team_ids = fields.Many2many(
        comodel_name='sale.stage.team',
        relation='res_users_sale_stage_team_rel',
        column1='user_id',
        column2='team_id',
        string='Sale Stage Teams',
        help="Team(s) assigned to this user. This determines which "
             "Sale Order stages the user is allowed to move an order "
             "to. Leave empty (and not System Administrator) to block "
             "the user from changing any stage."
    )
