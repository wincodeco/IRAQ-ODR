

from odoo import fields, models



class ResPartner(models.Model):
    _inherit = "res.partner"

    legal_name = fields.Char('Legal name')
    legal_type = fields.Selection(
        selection=[
            ('legal_entity', 'Legal Entity'),
            ('fop', 'FOP')
        ],
        string='Legal Type',
    )
    company_registry = fields.Char('Code EDRPOU')
    director = fields.Char()
    signature = fields.Binary(
        string='Signature',
        help='Partner Signature',
        attachment=True,
    )
    registration_certificate = fields.Char('Registration certificate')
    taxpayer_status_id = fields.Many2one(
        comodel_name='account.taxpayer_status',
        string='Taxpayer Status',
    )
    is_vat_payer = fields.Boolean('VAT payer')
    city = fields.Char(translate=True)

    def write(self, vals):
        result = super(ResPartner, self).write(vals)
        for record in self:
            if self.env.user.company_id.partner_id == record and \
                    record.company_registry != self.env.user.company_id.\
                    company_registry:
                self.env.user.company_id.company_registry = \
                    record.company_registry
        return result
