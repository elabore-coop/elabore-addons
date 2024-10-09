# Copyright 2023 Stéphan Sainléger (Elabore)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "elabore_subscription_price",
    "version": "16.0.1.0.0",
    "author": "Elabore",
    "website": "https://elabore.coop",
    "maintainer": "Elabore",
    "license": "AGPL-3",
    "category": "Tools",
    "summary": "Auto computation of subscription based on employees_number, services, and backup size",
    # any module necessary for this one to work correctly
    "depends": [
        "base",
        "subscription_oca", 
        "maintenance_server_data",
        "maintenance_project"
    ],
    "qweb": [],
    "external_dependencies": {
        "python": [],
    },
    # always loaded
    "data": [
        "views/res_partner_views.xml",
        "views/sale_subscription_views.xml",       
        "views/service_views.xml",       
    ],
    # only loaded in demonstration mode
    "demo": [],
    "js": [],
    "css": [],
    "installable": True,
    # Install this module automatically if all dependency have been previously
    # and independently installed.  Used for synergetic or glue modules.
    "auto_install": False,
    "application": False,
}