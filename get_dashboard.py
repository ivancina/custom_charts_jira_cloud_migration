import requests
from requests.auth import HTTPBasicAuth
import settings


def get_dashboard(dashboard_id: str) -> str:
    url = f"{settings.JIRA_MAIN_URL}/rest/api/3/dashboard/{dashboard_id}"

    auth = HTTPBasicAuth(settings.JIRA_EMAIL, settings.JIRA_TOKEN)
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


