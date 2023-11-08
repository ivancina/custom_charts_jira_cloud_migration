import requests
from requests.auth import HTTPBasicAuth
import json
from settings import JIRA_EMAIL, JIRA_TOKEN, JIRA_MAIN_URL
from get_accountId_for_user import get_instance_users

user_data = json.loads(get_instance_users())

def change_owner(display_name: str, dashboard_id: int):
    url = f"{JIRA_MAIN_URL}/rest/internal/latest/dashboards/changeOwner"

    auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    for user in user_data:
        if user["displayName"] == display_name:
            owner = user["accountId"]
            break
        else:
            return "There is no user with that name!"

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
