from odoo import models, fields, api

class SaleOrderStage(models.Model):
    _inherit = 'sale.order.stage'

    is_csr_stage = fields.Boolean(string="CSR's Team Stage", default=False)
    is_store_stage = fields.Boolean(string="Store Team Stage", default=False)
    is_purchase_stage = fields.Boolean(string="Purchase Team Stage", default=False)
    is_logistics_stage = fields.Boolean(string="Logistics Team Stage", default=False)

    is_current_user_stage_admin = fields.Boolean(
        compute='_compute_is_current_user_stage_admin'
    )

    @api.depends_context('uid')
    def _compute_is_current_user_stage_admin(self):
        is_admin = self.env.su or self.env.user.is_admin_stage_team
        for stage in self:
            stage.is_current_user_stage_admin = is_admin

