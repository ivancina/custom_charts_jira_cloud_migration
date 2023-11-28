import logging
import sys
import pandas as pd
from changeOwner import change_owner
from get_all_dashboards import get_dashboards_by_owner
from get_accountId_for_user import get_instance_users
import csv

logger = logging.getLogger(__name__)
logging.basicConfig(filename='log/custom-charts-cloud-migration-change-owner_new.log', filemode='w',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',
                    level=logging.DEBUG)

logger.info("------------------- ##### Starting ##### ------------------- ")
# excel_data = pd.read_excel("files/QBE_CustomCharts-v5.xlsx", "Custom Chart (PROD)")
excel_data = pd.read_csv("files/Sheet1-Table 1.csv", sep=';')
# Get total number of dashboards that Ivica Vancina is an owner

dashboards_by_owner = []
start = 0
dashboards = get_dashboards_by_owner("712020:fba73fc0-a3f7-4e6f-8da0-1c3b3e3d9ed1", start, dashboards_by_owner)
total = dashboards["total"]
while total >= start:
    start += 100
    dashboards = get_dashboards_by_owner("712020:fba73fc0-a3f7-4e6f-8da0-1c3b3e3d9ed1", start, dashboards_by_owner)

all_users = []
start = 0
total = 8778
while total >= start:
    start += 100
    users = get_instance_users(start, all_users)

# logger.info(f"------------------- ##### Number of users: {len(all_users)} ##### ------------------- ")
logger.info(f"------------------- ##### Number of dashboards: {len(dashboards_by_owner)} ##### ------------------- ")
#logger.info(f"------------------- ##### Users: {all_users} ##### ------------------- ")

with open("files/Ivica-dashboard 1.csv", "r") as file:
    reader = csv.reader(file)

    # Skip the header row
    next(reader)

    # Iterate over the rows
    for index, row in enumerate(reader, start=1):
        try:
            accountId = str(row[3])
            dashboard_id = str(row[0])
            logger.info("Owner Name: " + accountId)
            print("Owner mail: " + accountId)
            change = change_owner(accountId, dashboard_id)
            logging.info("Dashboard id: " + str(dashboard_id) + f" {accountId} is updated?: " + change)
        except Exception as e:
            logging.error("Something went wrong with: " + str(e))

logger.info("------------------- ##### Finished ##### ------------------- ")
sys.exit()
