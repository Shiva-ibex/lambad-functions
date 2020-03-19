## This lambda function deletes the snapshots based on retention period

## Deletes the snapshot based on snapshot creation time and retention period time

## No need of any tags to specified for snapshots, it only takes creation time for deletion


import boto3 
import collections 
import datetime
#from datetime import datetime
dbs = boto3.client('rds','us-east-2')
def lambda_handler(event, context):
    print('hi')
    reservations = dbs.describe_db_snapshots()
    print(reservations["DBSnapshots"])
    #print(reservations)
     # get the time
    now = datetime.datetime.today().strftime('%d%m%Y')
    print ('now')
    current = int(now)
    #print(current)
    retention = 2
    for snapshot in reservations["DBSnapshots"]:
    #    print(snapshot["DBSnapshotId"])
        print ("Checking snapshot %s which was created on %s" % (snapshot['DBSnapshotIdentifier'],snapshot['SnapshotCreateTime']))
        # Remove timezone info from snapshot in order for comparison to work below
        x = snapshot["SnapshotCreateTime"].strftime('%d%m%Y')
        print(x)
        snaptime = int(x)
        print (snaptime)
        z = current - snaptime
        print(z)
        if z > retention:
            print("The snapshot older than One day. Deleting Now")
            dbs.delete_db_snapshot(DBSnapshotIdentifier= snapshot['DBSnapshotIdentifier'])
        else:
            print("Snapshot is newer than configured retention of %d days so we keep it" % (retention))
