import json
import logging
import sys
import pandas as pd

from get_gadget_ids import get_gadgets_on_dashboard
from add_gadged_to_dashboard import add_gadget
from gadgets import SIMPLE_SEARCH, CUSTOM_CHART, ISSUE_LIST
from update_gadget import update_gadget
from search_for_dashboards_by_owner import get_dashboards_by_me

logger = logging.getLogger(__name__)
logging.basicConfig(filename='log/custom-charts-cloud-migration.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.DEBUG)

logger.info("------------------- ##### Starting ##### ------------------- ")
#excel_data = pd.read_excel("files/QBE_CustomCharts-v5.xlsx", "Custom Chart (PROD)")
excel_data = pd.read_csv("files/QBE_CustomCharts-v5 (1).csv", sep=';')
# Get total number of dashboards that Ivica Vancina is an owner
total = json.loads(get_dashboards_by_me(0))["total"]
logger.info(" ------------------- ##### Total number of dashboards on Jira cloud instance: " + str(total) + " ##### ------------------- ")

for index, row in excel_data.iterrows():
    get_dashboards_start = 0
    while get_dashboards_start <= total:
        dashboards = json.loads(get_dashboards_by_me(get_dashboards_start))["values"]
        logger.info("Total: " + total)
        for dashboard in dashboards:
            if dashboard['name'] == row["Dashboard Name"]:
                logging.info("We have a match!!")
                logging.info("Dashboard: " + str(dashboard))
                # try:
                #     if row["Gadget Type"] == "custom-chart":
                #         chart_type = CUSTOM_CHART
                #     elif row["Gadget Type"] == "issue-list":
                #         chart_type = ISSUE_LIST
                #     else:
                #         chart_type = SIMPLE_SEARCH
                #
                #     dashboard_id = dashboard["id"]
                #     logging.info("Dashboard Name: " + dashboard['name'])
                #     logging.info("dashboard_id: " + dashboard_id)
                #     logging.info("chart_type: " + chart_type)
                #     logging.info("Column: " + str(row["Column"]))
                #     logging.info("JSON: " + row["XML"])
                #     add = add_gadget(dashboard["id"], chart_type, row["Column"])
                #     load_gadget_json = json.loads(add)
                #     gadget_id = str(load_gadget_json["id"])
                #     logger.info("Gadget id: " + str(load_gadget_json))
                #     update = update_gadget(dashboard["id"], gadget_id, row["XML"])
                #     logger.info("Dashboard Name: " + row["Dashboard Name"] + "is updated?: " + update)
                #     break
                # except Exception as e:
                #     logging.error("Something went wrong with: " + dashboard['name'] + ": " + e)
                #     break

        get_dashboards_start += 100

    if get_dashboards_start == 400:
        get_dashboards_start = 0


sys.exit()
