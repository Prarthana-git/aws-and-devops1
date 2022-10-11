import boto3

client = boto3.client('s3')
#s3 = boto3.resource('s3')

#list of bucket
list_bucket=client.list_buckets()
print(list_bucket)

#bucket creation
response = client.create_bucket(
    Bucket='aws-s3-demo-prarthana',
)
print(response)

#upload file to s3 bucket

responseb = client.put_object(
    Body=open('boto.py','r').read(),
    Bucket='aws-s3-demo-prarthana',
    Key='boto.py',
)
print(responseb)


#dowload file from s3 bucket to local machine
response = client.get_object(
    Bucket='aws-s3-demo-prarthana',
    Key='boto.py',
)
print(response.get('Body').read().decode())

#list object
response = client.list_objects(
    Bucket='aws-s3-demo-prarthana',
)
objects = response.get("Contents")
print(f"Total objects :{len(objects)}")
print(objects)