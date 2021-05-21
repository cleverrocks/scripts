import boto3

ec2_client = boto3.client('ec2')

response = ec2_client.describe_instances()

instanceList = []

# This section will bring the Instance IDs for the account and region associated with Boto3 default configuration

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instanceList.append(instance["InstanceId"])


# This section will update the EC2 Settings to Enforce using V2 for Metadata service i.e
# https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-fsbp-controls.html#ec2-8-remediation

print(instanceList)

for instance in instanceList:
    response = ec2_client.modify_instance_metadata_options(
        InstanceId=instance,
        HttpTokens='required',
        HttpEndpoint='enabled',
        DryRun=False
    )
    print(response)
