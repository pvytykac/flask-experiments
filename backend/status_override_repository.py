import logging
from typing import Optional

data = {}

logger = logging.getLogger(__name__)


def list_status_overrides():
    return data


def save_status_override(project_id: int, status):
    logger.info(f"saving status override for project {project_id} to status {status}")

    data[project_id] = {
        "project_id": project_id,
        "status": status
    }


def remove_status_override(project_id: int):
    logger.info(f"deleting status override for project {project_id}")

    if project_id in data.keys():
        data.pop(project_id, None)


def get_status_override(project_id: int) -> Optional[dict]:
    logger.debug("looking up status overrides")

    if project_id in data.keys():
        return data[project_id]
    else:
        return None
