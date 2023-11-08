import requests
from requests.auth import HTTPBasicAuth
import settings


def get_jira_cloud_instance_dashboards(start_at: int) -> str:
    """
    :rtype: object
    """
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

print(get_jira_cloud_instance_dashboards(0))
