from odoo import models, fields, api

class Accounts(models.Model):
    _name = 'my_contacts.accounts'
    _description = 'Accounts'

    name = fields.Char(string='Account Name', required=True)

    parent_id = fields.Many2one('my_contacts.accounts', string='Parent Account')

    child_ids = fields.One2many('my_contacts.accounts', 'parent_id')
    child_count = fields.Integer(string='Number of Child Accounts', compute='_compute_child_count')

    lead_ids = fields.One2many('crm.lead', 'account_id')

    primary_contact = fields.Many2one('res.partner', string='Primary Contact')

    @api.depends('child_ids')
    def _compute_child_count(self):
        for rec in self:
            rec.child_count = len(rec.child_ids)


    def action_view_child_accounts(self):
        action = self.env["ir.actions.actions"]._for_xml_id("my_crm.accounts_action")  
        action['domain'] = [('id', 'in', self.child_ids.ids)] 
        return action      