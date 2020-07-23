# -*- coding: utf-8 -*-
{
    'name': "BradooEscolas",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['sale', 'hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/bradooescolas_class_view.xml',
        'views/bradooescolas_courses_view.xml',
        'views/bradooescolas_lessons_view.xml',
        'views/product_template_view.xml',
        'views/res_partner_view.xml',
        'views/bradooescolas_menu.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
}
