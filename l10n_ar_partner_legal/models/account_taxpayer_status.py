

from odoo import fields, models



class AccountTaxpayerStatus(models.Model):
    _name = "account.taxpayer_status"
    _description = 'Taxpayer Statuses'

    name = fields.Char(
        string='Status name',
    )
