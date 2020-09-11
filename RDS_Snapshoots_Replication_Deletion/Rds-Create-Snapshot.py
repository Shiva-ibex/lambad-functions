
// The below function Creates running rds snapshots based on given database environment names

### py run time 3.7


import json
import os
import boto3
import datetime
import json
client = boto3.client('rds')
start_date = str(datetime.datetime.now().strftime("%d-%m-%Y"))
#region = os.getenv("region")
def lambda_handler(event, context):
    dbs = json.loads(os.getenv("dbs"))
    for db in dbs:
        print(db)
        createdbsnapshot = client.create_db_snapshot(DBSnapshotIdentifier='lambdasnapshot-for-'+db+'-'+start_date,DBInstanceIdentifier=db)
        print(createdbsnapshot)
        #describingdbsnapshot = client.describe_db_snapshots(DBInstanceIdentifier='inspired')
        #print(describingdbsnapshot)
