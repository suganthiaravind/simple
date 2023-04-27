import boto3
import sys

#region = sys.argv[1]
#accesskey = sys.argv[2]
#secretkey = sys.argv[3]
region = "us-east-2"

#client = boto3.client('ec2',region_name=region,aws_access_key_id=accesskey,aws_secret_access_key=secretkey)
client = boto3.client('ec2',region_name=region)

data1 = client.describe_instances()
for data2 in data1["Reservations"]:
	for data13 in data2["Instances"]:
		print(data13)
