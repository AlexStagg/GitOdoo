# -*- coding: utf-8 -*-

{
    'name': 'Git Odoo',
    'version': '1.0',
    'author': 'Smart IT',
    'summary': 'Get Pull request info in Odoo',
    'description': "",
    'category': 'Smart Modules',
    'sequence': 2,
    'website': 'https://www.smart-ltd.co.uk',
    'depends': ["project", "helpdesk"],
    'data': [
        'views/helpdesk_ticket.xml',
        'views/project_task.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}
