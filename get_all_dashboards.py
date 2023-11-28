import requests
from requests.auth import HTTPBasicAuth
import settings


def get_jira_cloud_instance_dashboards(start_at: int) -> str:
    """ :rtype: object """
    url = f"{settings.JIRA_MAIN_URL}/rest/api/3/dashboard/search?maxResults=100&startAt={start_at}"
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

def get_dashboards_by_owner(owner, start_at, dashbords_data):
    url = f"{settings.JIRA_MAIN_URL}//rest/api/3/dashboard/search?accountId={owner}&maxResults=100&startAt={start_at}"
    headers = {
        "Accept": "application/json"
    }
    auth = HTTPBasicAuth(settings.JIRA_EMAIL, settings.JIRA_TOKEN)

    response = requests.get(url, headers=headers, auth=auth)

    if response.status_code == 200:
        dashboards = response.json()
        for dashboard in dashboards["values"]:
            dashbords_data.append(dashboard)
        return dashboards
    else:
        print("Failed to retrieve dashboards. Status code:", response.status_code)





