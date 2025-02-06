import logging

data = {}

logger = logging.getLogger(__name__)


def save_subscriptions(user_id: int, project_ids: list[int]):
    logger.info(f"updating status notification subscriptions for user {user_id} to {project_ids}")

    data[user_id] = {
        "project_ids": project_ids,
    }


def get_subscriptions_by_user_id(user_id: int):
    logger.debug(f"looking up notification subscriptions for user {user_id}")

    if user_id in data.keys():
        return data[user_id]
    else:
        return list()
