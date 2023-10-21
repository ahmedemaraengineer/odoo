from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Opportunity(models.Model):
    _inherit = 'crm.lead'

    account_id = fields.Many2one('my_contacts.accounts', string='Account', required=True)
	
    @api.onchange('stage_id')
    def _onchange_won(self):
        if self.stage_id.is_won:
            self.env['my_contacts.accounts'].create({'name': self.name})    

    @api.constrains('type')
    def _check_has_activities(self):
        for record in self:
            activity_ids = self.env['crm.activity.report'].search([('lead_id', '=', record.id)])
            if not activity_ids and record.type == 'opportunity':
                raise ValidationError("The lead must have at least one done activity")

            
