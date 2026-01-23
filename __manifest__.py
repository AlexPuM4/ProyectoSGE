# -*- coding: utf-8 -*-
{
    'name': "Banco",

    'summary': """
        Te permite gestionar tus cuentas y movimientos bancarios
        """,

    'description': """
        Modulo de Aplicacion de Banco
    """,

    'author': "Grupo4 de 2ºDAM",
    'website': "https://site.educa.madrid.org/ies.sanjuandelacruz.pozuelodealarcon/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/Bank.xml',
        'views/Customer.xml',
        'views/Account.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
