from odoo import api, fields, models

class GitPulls(models.Model):
    _name = "gitodoo.git_pulls"
    _description = "Table for storing git pull requests"

    link = fields.Char(string="Link", required=True)
    state = fields.Selection([
        ("draft", "Draft"),
        ("review", "Ready for Review"),
        ("merge", "Ready to merge"),
        ("merged", "Merged"),
        ("closed", "Closed"),
        ("rejected", "Review Rejected")
    ], string="State")
    merged_date = fields.Datetime("Merged Date")
    ticket_id = fields.Many2one(comodel_name="helpdesk.ticket", string="Ticket ID")
    task_id = fields.Many2one(comodel_name="project.task", string="Task ID")

    @api.onchange("state")
    def _onchange_state(self):
        if self.state == 'merged':
            self.merged_date = fields.Datetime.now()
        else:
            self.merged_date = False
