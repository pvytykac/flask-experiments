import logging
from typing import Optional

data = {
    1: {"id": 1, "name": "Data Plans", "group": "Blue", "status": "ERROR"},
    2: {"id": 2, "name": "Data Policy", "group": "Blue", "status": "WARN"},
    3: {"id": 3, "name": "Policy Evaluation", "group": "Blue", "status": "OK"},
    4: {"id": 4, "name": "Proxy", "group": "Green", "status": "WARN"},
    5: {"id": 5, "name": "Security", "group": "Red", "status": "OK"}
}

logger = logging.getLogger(__name__)


def find_by_id(project_id) -> Optional[dict]:
    logger.debug(f"looking up project with id = {project_id}")

    if project_id in data.keys():
        return data[project_id]
    else:
        return None


def list_projects():
    logger.debug("looking up all projects")

    return list(data.values())
