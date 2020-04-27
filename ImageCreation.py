import json
import os
import boto3
import datetime

start_date = str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
#region = os.getenv("region")
create_time = datetime.datetime.now()
create_fmt = create_time.strftime('%Y-%m-%d')
client = boto3.client('ec2',region)

def lambda_handler(event, context):
    instanceids = []
        
    reservations = client.describe_instances( Filters=[{ 'Name': 'tag:server', 'Values': ['patch']},], DryRun=False).get('Reservations', [])
    instances = sum([[i for i in r['Instances']]for r in reservations], [])
    print("Found %d instances that need backing up" % len(instances))
    #print(instance['InstanceId'])
    for instance in instances:
        print(instance['InstanceId'])
        AMIid = client.create_image(
                InstanceId=instance['InstanceId'],
                Name="Image for " + instance['InstanceId'] + " on " +
                create_fmt,
                Description="AMI created by Lambda for instance " +
                instance['InstanceId'] + " from " + create_fmt,
                NoReboot=True,
                DryRun=False)
