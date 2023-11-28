import requests
from requests.auth import HTTPBasicAuth

from settings import JIRA_TOKEN, JIRA_EMAIL, JIRA_MAIN_URL

def get_instance_users(start_at: int, user_data: list):
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
    if response.status_code == 200:
        users_value = response.json()
        for user in users_value:
            if "emailAddress" in user:
                user_data.append(user)
        return users_value
    else:
        print("Failed to retrieve users. Status code:", response.status_code)

    return response.text



