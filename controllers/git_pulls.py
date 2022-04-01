import json
import re

from odoo import http
from odoo.http import request

regex = re.compile(r"(Ticket|Task): ([0-9]+).*")

class GitPullsController(http.Controller):
    @http.route('/git_pulls', type='json', methods=['POST'], auth='none', csrf=False)
    def git_pulls(self):
        data = json.loads(request.httprequest.data)
        headers = request.httprequest.headers

        event_name = headers.get('X-Github-Event', None)
        if not event_name:
            return

        title = data["pull_request"]["title"]
        pr_type, ref_id = regex.match(title).groups(1, 2)

        if event_name == 'pull_request_review':
            if data["action"] == "submitted":
                state = 'merge'
            elif data["action"] == "dismissed":
                state = 'rejected'
            else:
                state = 'review'

            pr = request.env["gitodoo.git_pulls"].search(['link', 'like', data["pull_request"]["html_url"]])
            if not pr:
                request.env["gitodoo.git_pulls"].create({
                    'link': data["pull_request"]["html_url"],
                    'state': state,
                    'ticket_id': ref_id if pr_type == 'Ticket' else False,
                    'task_id': ref_id if pr_type == 'Task' else False,
                })
            else:
                pr.state = state
        elif event_name == "pull_request":
            state = None
            if data["action"] == 'opened':
                if data["pull_request"]["state"] == "open":
                    state = "review"
                else:
                    state = "draft"
            elif data["action"] == 'converted_to_draft':
                state = "draft"
            elif data["closed"]:
                if data["merged"]:
                    state = "merged"
                else:
                    state = "closed"
            elif data["ready_for_review"]:
                state = "review"

            pr = request.env['gitodoo.git_pulls'].search(['link', 'like', data["pull_request"]["html_url"]])
            if not pr:
                request.env['gitodoo.git_pulls'].create({
                    'link': data['pull_request']['html_url'],
                    'state': state,
                    'ticket_id': ref_id if pr_type == 'Ticket' else False,
                    'task_id': ref_id if pr_type == 'Task' else False,
                })
            else:
                pr.state = state
        return
