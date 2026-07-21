{
    'name': 'Sale Order Stage Team Access',
    'version': '18.0.1.0.0',
    'summary': 'Restrict Sale Order stage movement based on Team assignment (Admin, CSR, Store, Purchase, Logistics)',
    'description': """
Sale Order Stage Team Access
=============================
This module restricts which Sale Order stages a user is allowed to move
an order to, based on the Team(s) assigned to that user in User
Preferences / Settings > Users.

Features
--------
* New "Sale Stage Teams" configuration menu with 5 default teams:
  Admin, CSR's Team, Store Team, Purchase Team, Logistics Team.
  (Fully editable - you can rename, add, or remove teams any time.)
* Each Team record has a list of "Allowed Stages" (Many2many to your
  existing Sale Order Stage model).
* Users form / My Profile gets a new "Stage Access" tab with checkboxes
  to assign one or more Teams to a user.
* A user assigned to the "Admin" team (is_admin_team = True), or any
  real Odoo System Administrator, can move a Sale Order to ANY stage -
  no restriction.
* A user assigned to CSR's / Store / Purchase / Logistics team can ONLY
  move Sale Orders to the stage(s) allowed for their team(s). Trying to
  move an order to any other stage raises a clear error popup and
  blocks the change.
* Restriction applies everywhere the stage is changed - Kanban
  drag & drop, list view quick edit, form view, everything - because it
  is enforced in the model's write() method, not in the UI.

IMPORTANT - please verify before installing
---------------------------------------------
This module assumes:
  1. Your existing custom Sale Order Stage model (the one you built,
     shown in your Kanban Stages list: Received, Confirmed, On Hold,
     Ready, Packed, Dispatched, Delivered, etc.) has technical name:
         sale.order.stage
  2. The Sale Order (sale.order) has a Many2one field named:
         stage_id
     pointing to that stage model.

If your actual model/field technical names are different, open:
  - models/sale_order.py
  - models/sale_stage_team.py
  - views/sale_stage_team_views.xml
and replace 'sale.order.stage' / 'stage_id' with your real names
before installing.
    """,
    'category': 'Sales',
    'author': 'Custom Development',
    'depends': ['sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_stage_team_views.xml',
        'views/res_users_views.xml',
        'data/team_data.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
