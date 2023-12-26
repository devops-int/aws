import json

import boto3

def lambda_handler(event, context):
    # Define your S3 bucket name and file name
    bucket_name = 'pphhllmm'
    file_name = 'information'

    # Create an EC2 client
    ec2_client = boto3.client('ec2')

    # Get a list of VPCs
    vpcs = ec2_client.describe_vpcs()

    # Get a list of subnets
    subnets = ec2_client.describe_subnets()

    # Create content to be written to the file
    content = "VPCs:\n"
    for vpc in vpcs['Vpcs']:
        content += f"VPC ID: {vpc['VpcId']}, CIDR Block: {vpc['CidrBlock']}\n"

    content += "\nSubnets:\n"
    for subnet in subnets['Subnets']:
        content += f"Subnet ID: {subnet['SubnetId']}, CIDR Block: {subnet['CidrBlock']}, VPC ID: {subnet['VpcId']}\n"

    # Create an S3 client
    s3_client = boto3.client('s3')

    # Put the content into the S3 object
    s3_client.put_object(Body=content, Bucket=bucket_name, Key=file_name)

    return {
        'statusCode': 200,
        'body': 'File created successfully!'
    }