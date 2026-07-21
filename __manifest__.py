{
    'name': 'Sale Order Stage Team Access',
    'version': '19.0.1.0.0',
    'summary': 'Restrict Sale Order stage movement based on Team Assignment Checkboxes',
    'description': """
Sale Order Stage Team Access
=============================
Restrict which Sale Order stages a user is allowed to move an order to.
Uses checkboxes on User Profiles and Stage configurations.

Features:
- Adds 5 checkboxes to the User Settings: Admin, CSR's Team, Store Team, Purchase Team, Logistics Team.
- Adds 4 checkboxes to Sale Order Stages to classify them for teams.
- Validates stage movement (Kanban and Form View) to ensure users only move to allowed stages.
- Automatically handles existing stages out of the box based on the provided names.
    """,
    'category': 'Sales',
    'author': 'Custom Development',
    'depends': ['sale_management', 'sale_order_stage_management'],
    'data': [
        'views/sale_order_stage_views.xml',
        'views/res_users_views.xml',
        'views/sale_order_views.xml',
    ],
    'post_init_hook': 'post_init_hook',
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
