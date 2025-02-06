from typing import Optional

data = {
    1: {"id": 1, "username": "paly", "password": "pA$$w0rd"},
    2: {"id": 2, "username": "paly2", "password": "pA$$w0rd2"}
}


def lookup_by_credentials(username: str, password: str) -> Optional[dict]:
    for user in data.values():
        if user['username'] is username and user['password'] is password:
            return user

    return None
