import json
import logging
import sys
import pandas as pd
from changeOwner import change_owner
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
        for dashboard in dashboards:
            if dashboard['name'] == row["Dashboard Name"]:
                logging.info("We have a match!!")
                try:
                    owner_name = row["Owner"]
                    logger.info("Owner Name: " + owner_name)
                    change = change_owner(owner_name, dashboard["id"])
                    logging.info("Dashboard Name: " + row["Dashboard Name"] + "owner is updated?: " + change)
                    break
                except Exception as e:
                    logging.error("Something went wrong with: " + dashboard['name'] + ": " + str(e))
                    break

        get_dashboards_start += 100

    if get_dashboards_start == 400:
        get_dashboards_start = 0


sys.exit()
