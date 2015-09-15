# -*- coding: utf-8 -*-
{
    'name': "Custom models for MRP",
    'author': "Ivan Yelizariev",
    'website' : "https://yelizariev.github.io",
    'category': 'Manufacturing',
    'version': '1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['mrp'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'view.xml',
    ],
    "installable": True
}
