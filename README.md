# GitOdoo - Attach your github pull requests to odoo tickets and tasks

## Setup
To get the module setup you should first install the module.
Then create a github webhook on either the repos you want to enable the service on, or your orginasation.
Only the "Pull Requests" and "Pull Request Reviews" events are necessary, and the content type should be json.

Now, whenever a PR on an enabled repo is created, and the title starts with either "Ticket {helpdesk ticket id}:" or "Task {project task id}:" the PR will be added to the pull requests tabs on the resources.

## Features
- New PRs are added to tickets/tasks when raised.
- PRs are automatically marked as rejected.
- PRs are automatically marked as merged.
- PRs are automatically marked when ready for review.
- PRs are automatically marked when review is accepted as ready to merge.
- PRs are automatically marked when review is rejected as rejected.
- PRs are automaticallt marked when they are ready for review (not draft and not rejected).
