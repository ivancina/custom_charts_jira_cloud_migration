import requests
from requests.auth import HTTPBasicAuth
from settings import JIRA_TOKEN, JIRA_EMAIL, JIRA_MAIN_URL


def get_gadgets() -> str:
    url = f"{JIRA_MAIN_URL}/rest/api/3/dashboard/gadgets"

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


print(get_gadgets())