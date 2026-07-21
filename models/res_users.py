from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    is_admin_stage_team = fields.Boolean(
        string="Admin Stage Team",
        help="Full access to move Sale Orders to ANY stage."
    )
    is_csr_stage_team = fields.Boolean(
        string="CSR's Stage Team",
        help="Access to CSR's Team stages."
    )
    is_store_stage_team = fields.Boolean(
        string="Store Stage Team",
        help="Access to Store Team stages."
    )
    is_purchase_stage_team = fields.Boolean(
        string="Purchase Stage Team",
        help="Access to Purchase Team stages."
    )
    is_logistics_stage_team = fields.Boolean(
        string="Logistics Stage Team",
        help="Access to Logistics Team stages."
    )
