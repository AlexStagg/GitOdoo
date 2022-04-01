from odoo import fields, models, api


class Task(models.Model):
    _inherit = "project.task"

    pull_request = fields.One2many(comodel_name='smart.git_pulls', inverse_name='task_id', string='Pull Request')
