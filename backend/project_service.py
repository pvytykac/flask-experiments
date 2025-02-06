from backend import status_override_repository, projects_repository, status_notification_subscription_repository


def list_project_groups(user_id):
    subscriptions = get_subscriptions_by_user_id(user_id)
    status_overrides = list_status_overrides()
    projects = projects_repository.list_projects()
    groups = list()

    for project in projects:
        if project['id'] in status_overrides.keys():
            status_override = status_overrides[project['id']]['status']
            effective_status = status_override
        else:
            status_override = None
            effective_status = project['status']

        enriched_project = {
            "id": project['id'],
            "name": project['name'],
            "subscribed": project['id'] in subscriptions,
            "effectiveStatus": effective_status,
            "statusReported": project['status'],
            "statusOverride": status_override
        }

        if next((group for group in groups if group['name'] is project['group']), None) is None:
            groups.append({"name": project['group'], "projects": list()})

        next(group for group in groups if group['name'] is project['group'])['projects'].append(enriched_project)

    return {"groups": groups}


def get_status_override(project_id):
    return status_override_repository.get_status_override(project_id)


def list_status_overrides():
    return status_override_repository.list_status_overrides()


def save_status_override(project_id, status):
    status_override_repository.save_status_override(project_id, status)


def remove_status_override(project_id):
    status_override_repository.remove_status_override(project_id)


def get_subscriptions_by_user_id(user_id):
    return status_notification_subscription_repository.get_subscriptions_by_user_id(user_id)


def save_status_change_subscriptions(user_id, project_ids):
    status_notification_subscription_repository.save_subscriptions(user_id, project_ids)
