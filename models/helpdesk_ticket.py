from odoo import fields, models, api


class HelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    pull_request = fields.One2many(comodel_name='smart.git_pulls', inverse_name='ticket_id', string='Pull Request')