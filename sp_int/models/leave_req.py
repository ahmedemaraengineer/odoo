from odoo import models, fields 
from odoo.exceptions import ValidationError
import requests


class LeaveReq(models.Model):
    _inherit = 'hr.leave'

    def validate_req(self):
        data = {'ids': [], 'from': [], 'to': []}
        for leave in self:
            data['ids'].append(leave.employee_id.name)
            data['from'].append(leave.date_from)
            data['to'].append(leave.date_to)

        out = [data[i] for i in data]    
        raise ValidationError(out)


