import requests
from requests.auth import HTTPBasicAuth
from settings import JIRA_EMAIL, JIRA_TOKEN, JIRA_MAIN_URL


def update_gadget(dashboard_id: str, gadget_id: str, payload: object):
    url = f"{JIRA_MAIN_URL}/rest/api/2/dashboard/{dashboard_id}/items/{gadget_id}/properties/params?_r=1695727815847"
    auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = payload

    response = requests.request(
        "PUT",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )
    return response.text
