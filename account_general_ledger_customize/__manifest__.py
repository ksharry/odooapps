# -*- coding: utf-8 -*-
{
    'name': 'account_general_ledger_customize',
    'version': '13.0.1.0.0',
    'summary': '總分類帳串查與餘額查詢',
    'sequence': -100,
    'description': """總分類帳串查與餘額查詢""",
    'category': 'Accounting/Accounting',
    'author': 'Harry Chang',
    'maintainer': 'Harry Chang',
    'license': 'LGPL-3',
    'depends': ['base', 'account'],
    'data': [
        'views/account_move.xml'
    ],
    'demo': [],
    'qweb': [],
    'images': ['static/description/banner.png'],
    'intallable': True,
    'application': True,
    'auto_install': False,
}