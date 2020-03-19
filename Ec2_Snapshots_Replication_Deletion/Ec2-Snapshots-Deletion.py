## This lambda function deletes the snapshots based on retention period

## Deletes the snapshot based on snapshot creation time and retention period time

## No need of any tags to specified for snapshots, it only takes creation time for deletion


import boto3 
import collections 
import datetime
#from datetime import datetime
ec = boto3.client('ec2','us-east-2')
def lambda_handler(event, context):
    print('hi')
    reservations = ec.describe_snapshots(OwnerIds=["self"])
    print(reservations["Snapshots"])
    # get the time
    now = datetime.datetime.today().strftime('%Y%m%d')
    print ('now')
    current = int(now)
    retention = 1
    for snapshot in reservations["Snapshots"]:
        #print(snapshot["SnapshotId"])
        print ("Checking snapshot %s which was created on %s" % (snapshot['SnapshotId'],snapshot['StartTime']))
        # Remove timezone info from snapshot in order for comparison to work below
        x = snapshot["StartTime"].strftime('%Y%m%d')
        print(x)
        snaptime = int(x)
        print (snaptime) 
        z = current - snaptime
        print(z)
        if z > retention:
            print("The snapshot older than One day. Deleting Now")
            ec.delete_snapshot(SnapshotId= snapshot['SnapshotId'])
        else:
            print("Snapshot is newer than configured retention of %d days so we keep it" % (retention))
