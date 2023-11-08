import requests
from requests.auth import HTTPBasicAuth
import json
from settings import JIRA_TOKEN, JIRA_EMAIL, JIRA_MAIN_URL


def add_gadget(dashboard_id: str, gadget_class: str, column: int):
    url = f"{JIRA_MAIN_URL}/rest/api/2/dashboard/{dashboard_id}/gadget"

    auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps({
        "ignoreUriAndModuleKeyValidation": False,
        "moduleKey": gadget_class,
        "position": {
            "column": column,
        }
    })

    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )

    return response.text
