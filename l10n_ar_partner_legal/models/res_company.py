

from odoo import fields, models



class ResCompany(models.Model):
    _inherit = "res.company"

    director = fields.Char(
        related='partner_id.director',
        string='Director',
    )
    registration_certificate = fields.Char(
        string='Registration certificate',
        related='partner_id.registration_certificate',
    )
    taxpayer_status_id = fields.Many2one(
        related='partner_id.taxpayer_status_id',
        string='Taxpayer status',
    )

    def write(self, vals):
        """ Save the company_registry to partner_id on changing. """
        result = super(ResCompany, self).write(vals)
        for record in self:
            if record.company_registry != record.partner_id.company_registry:
                record.partner_id.company_registry = record.company_registry
        return result
