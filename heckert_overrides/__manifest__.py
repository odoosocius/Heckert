# -*- coding: utf-8 -*-
{
    # Module information
    'name': 'Heckert Overrides',

    'summary': 'Contains overrides and customizations.',
    'description': """
Heckert Overrides 
     Allows to override and customize the odoo backend without loosing the customization on update. 
    """,

    # Author
    'author': 'git GmbH',
    'developer': 'Guido Palacios',
    'website': 'https://odoo.heckert-original.com',
    'maintainer': 'git GmbH',
    "support": "info@gitgmbh.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'sale',
    'version': '12.0.1',
    'license': 'OPL-1',

    # any module necessary for this one to work correctly
    'depends': ['base',
        'sale',
    ],

    # always loaded
    'data': [
        'views/sale_order_views.xml',
        'views/text_block.xml',
        'security/ir.model.access.csv'
        #'templates/assets.xml',
        #'views/template.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        #'views/demo.xml',
    ],

    # Technical
    'installable': True,
    'auto_install': False,
}
