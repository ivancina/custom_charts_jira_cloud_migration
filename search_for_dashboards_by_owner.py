import requests
from requests.auth import HTTPBasicAuth
from settings import JIRA_TOKEN, JIRA_EMAIL, JIRA_MAIN_URL


# Getting all dashboards that Ivica Vancina is an owner
def get_dashboards_by_me(start_at: int) -> str:
    """
    :rtype: object
    """
    url = f"{JIRA_MAIN_URL}/rest/api/3/dashboard/search?startAt={start_at}&maxResults=100&accountId=712020:fba73fc0-a3f7-4e6f-8da0-1c3b3e3d9ed1"

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