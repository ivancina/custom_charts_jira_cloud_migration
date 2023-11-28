import requests
from requests.auth import HTTPBasicAuth
import json
from settings import JIRA_EMAIL, JIRA_TOKEN, JIRA_MAIN_URL


def change_owner(accountId: str, dashboard_id: int):
    url = f"{JIRA_MAIN_URL}/rest/internal/latest/dashboards/changeOwner"

    auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    owner = accountId
    payload = json.dumps({
                    "accountId": owner,
                    "dashboardId": dashboard_id
            })

    response = requests.request(
                    "PUT",
                    url,
                    data=payload,
                    headers=headers,
                    auth=auth
                )
    return response.text



