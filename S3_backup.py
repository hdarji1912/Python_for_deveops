# This is a script to take backup files from a local directory to an AWS S3 bucket using Boto3 library in Python.
# boto3 is the Amazon Web Services (AWS) SDK for Python, which allows Python developers to write software that makes use of services like Amazon S3 and Amazon EC2.
import boto3

region = "us-east-2"

s3 = boto3.resource("s3", region_name=region)

bucket_name = "python-for-deveops"

s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        "LocationConstraint": region
    }
)

print("Bucket created successfully")