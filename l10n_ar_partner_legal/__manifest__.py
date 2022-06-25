
{
    'name': 'IRAQ ODR',
    'version': '15.0',
    'category': 'Localization',
    'author': 'Wincode',
    'maintainer': 'Wincode',
    'price': '140.0',
    'currency': 'USD',
    'website': 'https://wincode.io',
    'license': 'LGPL-3',
    'summary': 'Iraq Official Documentation Requirements',
    'images': ['static/description/banner.png'],
    'live_test_url': 'https://wincode.io',
    'depends': [
        'account',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'data/taxpayer_status_data.xml',
        'views/res_company_views.xml',
        'views/res_partner_views.xml',
    ],
    'external_dependencies': {
    },
    'support': 'support@wincode.io',
    'application': True,
    'installable': True,
    'auto_install': False,
}
