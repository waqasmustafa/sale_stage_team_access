from odoo import api, SUPERUSER_ID

def post_init_hook(env):
    """
    Initialize the stage permissions automatically based on the stage names
    from the provided list. This makes it work out of the box.
    """
    # CSR's Team Stages
    csr_names = [
        'Received', 'Confirm', 'Confirmed', 'On Hold', 'Payment Pending', 'Pending Payment', 
        'Customer Cancelled', 'Cancel', 'Cancelled', 'Duplicate', 'Not Answering', 
        'Critical Order', 'Critical Orders', 'Urgent Orders'
    ]
    env['sale.order.stage'].search([('name', 'in', csr_names)]).write({'is_csr_stage': True})

    # Store Team Stages
    store_names = ['Ready', 'Stock Awaiting']
    env['sale.order.stage'].search([('name', 'in', store_names)]).write({'is_store_stage': True})

    # Purchase Team Stages
    purchase_names = ['Stock Available']
    env['sale.order.stage'].search([('name', 'in', purchase_names)]).write({'is_purchase_stage': True})

    # Logistics Team Stages
    logistics_names = [
        'Pack', 'Packed', 'TBD', 'Return Receive', 'Return Received', 
        'Return Initiated', 'Returns Initiated', 'Stock Punch', 'Load Sheet', 
        'Parcel Tracking', 'Dispatched', 'Delivered'
    ]
    env['sale.order.stage'].search([('name', 'in', logistics_names)]).write({'is_logistics_stage': True})
