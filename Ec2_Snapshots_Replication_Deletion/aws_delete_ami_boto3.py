#!/usr/bin/env python

###########3  Delete/Deregister 30 days old AMI in AWS using boto3 and python  #############

####### USE ON YOUR OWN RISK - THIS IS GOING TO DEREGISTER AMI OLDER THAN 30 DAYS #########
#### Runtime Python 2.7 ####


import boto3
from dateutil.parser import parse
import datetime
age = 30
aws_profile_name = 'prod'
def days_old(date):
    get_date_obj = parse(date)
    date_obj = get_date_obj.replace(tzinfo=None)
    diff = datetime.datetime.now() - date_obj
    return diff.days

boto3.setup_default_session(profile_name = aws_profile_name)
ec2 = boto3.client('ec2')
amis = ec2.describe_images(Owners=[
        'self'
    ])
for ami in amis['Images']:
    create_date = ami['CreationDate']
    ami_id = ami['ImageId']
    # print ami['ImageId'], ami['CreationDate']
    day_old = days_old(create_date)
    if day_old > age:
        print "deleting -> " + ami_id + " - create_date = " + create_date
        # deregister the AMI
        ec2.deregister_image(ImageId=ami_id)
