# -*- coding: utf-8 -*-
# Part of Hadoopt Technologies Private Limited. See LICENSE file for full copyright and licensing details.

{
    'name': 'Session',
    'version': '1.0',
    'author': 'Hadoopt Technologies Private Limited',
    'website': 'https://hadoopt.com',
    'category': 'Tools',
    'application': True,
    'maintainer': 'Hadoopt Technologies Private Limited',
    'license': 'AGPL-3',
    'summary': 'Session timeout based on number of sessions/user',
    'description':
        """
        This module allows admin to control the number of sessions the user is allowed to have.
        """,
    'depends': ['base', 'web'],    
    'data': [
        'security/ir.model.access.csv',
        'views/res_users_views.xml',
    ],
    "cloc_exclude": [
        '**/*'
    ],
    'images': ['static/images/main_screenshot.png'],
    'installable': True,
    'auto_install': False,
}
