import base64
from typing import Optional

from flask import Flask, make_response, request

from backend import user_repository, project_service

app = Flask(__name__)


# PROJECTS


@app.get("/project-groups")
def list_projects():
    user_id = get_user_id_from_request()
    return project_service.list_project_groups(user_id)


# STATUS OVERRIDES


@app.get("/projects/<int:project_id>/status-override")
def get_status_override(project_id: int):
    status_override = project_service.get_status_override(project_id)
    if status_override is None:
        return make_response({"error": "not found"}, 404)
    else:
        return status_override


@app.put("/projects/<int:project_id>/status-override")
def put_status_override(project_id: int):
    status = request.json['status']
    print(f"{project_id} {status}")
    project_service.save_status_override(project_id, status)

    return make_response({}, 204)


@app.delete("/projects/<int:project_id>/status-override")
def delete_status_override(project_id: int):
    project_service.remove_status_override(project_id)

    return make_response({}, 204)


# NOTIFICATION SUBSCRIPTIONS


@app.get("/me/status-change-subscriptions")
def get_status_notification_subscriptions():
    user_id = get_user_id_from_request()

    return project_service.get_subscriptions_by_user_id(user_id)


@app.put("/me/status-change-subscriptions")
def put_status_notification_subscriptions():
    user_id = get_user_id_from_request()
    project_ids = request.json['project_ids']

    project_service.save_status_change_subscriptions(user_id, project_ids)
    return make_response('', 204)


def get_user_id_from_request() -> Optional[int]:
    basic_auth = request.headers.get('Authorization').split(' ')[1].encode("ascii")
    decoded = (base64.b64decode(basic_auth).decode("ascii").split(':'))

    username: str = decoded[0]
    password: str = decoded[1]

    user = user_repository.lookup_by_credentials(username, password)
    if user is None:
        return None
    else:
        return user['id']
