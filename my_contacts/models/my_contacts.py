from odoo import fields, models, api
from odoo.exceptions import ValidationError

class MyContacts(models.Model):
    _inherit = 'res.partner'

    company_size = fields.Selection(string='Company Size', selection=[('sme', 'SME'), ('corporate', 'Corporate')])
  

    @api.constrains('is_company')
    def _check_is_company(self):
        for record in self:
            if record.is_company == True and not self.company_size:
                raise ValidationError("Company size must be set for company contacts")