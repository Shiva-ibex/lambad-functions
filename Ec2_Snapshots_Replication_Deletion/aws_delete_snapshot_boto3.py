##### This lambda function deletes the snapshots basedon time creation

#### it uses the py - 3.6 runtime

import boto3
import datetime
client = boto3.client('ec2',region_name='us-west-2')
snapshots = client.describe_snapshots(OwnerIds=['self'])
for snapshot in snapshots['Snapshots']:
    a= snapshot['StartTime']
    b=a.date()
    c=datetime.datetime.now().date()
    d=c-b
    try:
        if d.days>30:
            id = snapshot['SnapshotId']
            client.delete_snapshot(SnapshotId=id)
    except Exception:
        if 'InvalidSnapshot.InUse' in e.message:
            print("skipping this snapshot")
            continue
