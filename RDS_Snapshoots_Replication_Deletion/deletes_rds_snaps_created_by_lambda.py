#### deletes the rds snapsshots basedon creation time retention period

### It deletes the snaps created by lambda based on description

### run time py - 3.7


import json
import boto3
import datetime
from datetime import datetime, timedelta, tzinfo
class Zone(tzinfo):
    def __init__(self,offset,isdst,name):
        self.offset = offset
        self.isdst = isdst
        self.name = name
    def utcoffset(self, dt):
        return timedelta(hours=self.offset) + self.dst(dt)
    def dst(self, dt):
        return timedelta(hours=1) if self.isdst else timedelta(0)
    def tzname(self,dt):
        return self.name
UTC = Zone(10,False,'UTC')
retentionDate = datetime.now(UTC) - timedelta(days=4)
def lambda_handler(event, context):
    print("Connecting to RDS")
    rds = boto3.setup_default_session(region_name='us-west-2')
    client = boto3.client('rds')
    snapshots = client.describe_db_snapshots(SnapshotType='manual')
    print('Deleting all DB Snapshots older than %s' % retentionDate)
    for i in snapshots['DBSnapshots']:
        if i['Status'] == 'available' and i['SnapshotCreateTime'] < retentionDate and 'lambdasnapshot-' in i['DBSnapshotIdentifier'] :
            print ('Deleting snapshot %s' % i['DBSnapshotIdentifier'])
            client.delete_db_snapshot(DBSnapshotIdentifier=i['DBSnapshotIdentifier'])
