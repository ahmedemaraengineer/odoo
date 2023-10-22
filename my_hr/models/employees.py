from odoo import models, fields

class MyEmployee(models.Model):
    _inherit = 'hr.employee'

    custom_id = fields.Integer()