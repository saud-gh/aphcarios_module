# -*- coding: utf-8 -*-
{
    'name': "Aphcarios",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Description of module
    """,

    'author': "Aphcarios Engineering Solutions",
    'website': "https://www.aphcarios.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        # 'views/aphcarios_project_overview_view.xml',
        'views/aphcarios_project_views.xml',
        'views/aphcarios_project_menu.xml',
        'views/extended_product_views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
