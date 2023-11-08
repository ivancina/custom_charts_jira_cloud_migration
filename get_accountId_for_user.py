import requests
from requests.auth import HTTPBasicAuth

from settings import JIRA_TOKEN, JIRA_EMAIL, JIRA_MAIN_URL


def get_instance_users(start_at: int):
    url = f"{JIRA_MAIN_URL}/rest/api/3/users/search?maxResults=100&startAt={start_at}"

    auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_TOKEN)

    headers = {
        "Accept": "application/json"
    }

    response = requests.request(
        "GET",
        url,
        headers=headers,
        auth=auth
    )

    return response.text

