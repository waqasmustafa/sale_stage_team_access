# -*- coding: utf-8 -*-
from odoo import models, fields, api


class SaleStageTeam(models.Model):
    """Represents a Team (Admin, CSR's Team, Store Team, Purchase Team,
    Logistics Team) and the list of Sale Order Stages that team is
    allowed to move an order to.
    """
    _name = 'sale.stage.team'
    _description = 'Sale Order Stage Team'
    _order = 'sequence, id'

    name = fields.Char(string='Team Name', required=True)
    sequence = fields.Integer(string='Sequence', default=10)
    active = fields.Boolean(string='Active', default=True)

    is_admin_team = fields.Boolean(
        string='Full Access (Admin)',
        help="Users who belong to this team can move a Sale Order to "
             "ANY stage, without restriction. Use this only for the "
             "'Admin' team."
    )

    # NOTE: 'sale.order.stage' below must match the technical name of
    # your existing custom Sale Order Stage model. Change it here if
    # your model name is different.
    stage_ids = fields.Many2many(
        comodel_name='sale.order.stage',
        relation='sale_stage_team_stage_rel',
        column1='team_id',
        column2='stage_id',
        string='Allowed Stages',
        help="The Sale Order stages that members of this team are "
             "allowed to move an order into."
    )

    user_ids = fields.Many2many(
        comodel_name='res.users',
        relation='res_users_sale_stage_team_rel',
        column1='team_id',
        column2='user_id',
        string='Users',
        help="Users who belong to this team."
    )

    user_count = fields.Integer(
        string='Users',
        compute='_compute_user_count'
    )

    @api.depends('user_ids')
    def _compute_user_count(self):
        for team in self:
            team.user_count = len(team.user_ids)
