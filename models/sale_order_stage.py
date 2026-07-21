from odoo import models, fields

class SaleOrderStage(models.Model):
    _inherit = 'sale.order.stage'

    is_csr_stage = fields.Boolean(string="CSR's Team Stage", default=False)
    is_store_stage = fields.Boolean(string="Store Team Stage", default=False)
    is_purchase_stage = fields.Boolean(string="Purchase Team Stage", default=False)
    is_logistics_stage = fields.Boolean(string="Logistics Team Stage", default=False)
