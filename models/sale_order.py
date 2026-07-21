from odoo import models, fields, api, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    allowed_stage_ids = fields.Many2many(
        'sale.order.stage', 
        compute='_compute_allowed_stage_ids',
        store=False
    )

    @api.depends('stage_id') # We just need it to trigger on load
    def _compute_allowed_stage_ids(self):
        user = self.env.user
        if self.env.su or user.is_admin_stage_team:
            # Full access, all stages allowed
            all_stages = self.env['sale.order.stage'].search([])
            for order in self:
                order.allowed_stage_ids = all_stages
            return

        domain = []
        if user.is_csr_stage_team:
            domain.append(('is_csr_stage', '=', True))
        if user.is_store_stage_team:
            domain.append(('is_store_stage', '=', True))
        if user.is_purchase_stage_team:
            domain.append(('is_purchase_stage', '=', True))
        if user.is_logistics_stage_team:
            domain.append(('is_logistics_stage', '=', True))

        if not domain:
            for order in self:
                # Need to allow current stage at least so it doesn't break form view load
                order.allowed_stage_ids = order.stage_id if order.stage_id else False
            return

        # Combine domains with OR
        final_domain = ['|'] * (len(domain) - 1) + domain
        allowed_stages = self.env['sale.order.stage'].search(final_domain)

        for order in self:
            # Always allow the current stage to prevent form view from breaking when viewing an order 
            # in a stage the user can't move to (but they might just be viewing the order).
            if order.stage_id and order.stage_id not in allowed_stages:
                order.allowed_stage_ids = allowed_stages | order.stage_id
            else:
                order.allowed_stage_ids = allowed_stages

    def write(self, vals):
        if 'stage_id' in vals and vals.get('stage_id'):
            self._check_stage_team_access(vals['stage_id'])
        return super(SaleOrder, self).write(vals)

    def _check_stage_team_access(self, new_stage_id):
        user = self.env.user
        if self.env.su:
            return

        if user.is_admin_stage_team:
            return

        stage = self.env['sale.order.stage'].browse(new_stage_id)
        
        # Check if user has permission for this specific stage
        allowed = False
        if stage.is_csr_stage and user.is_csr_stage_team:
            allowed = True
        elif stage.is_store_stage and user.is_store_stage_team:
            allowed = True
        elif stage.is_purchase_stage and user.is_purchase_stage_team:
            allowed = True
        elif stage.is_logistics_stage and user.is_logistics_stage_team:
            allowed = True

        if not allowed:
            raise UserError(_(
                "You are not allowed to move this order to the '%(stage)s' stage.\n"
                "Please contact your administrator if you believe this is a mistake."
            ) % {'stage': stage.name})
