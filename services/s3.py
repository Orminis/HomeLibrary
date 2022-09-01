import boto3
from decouple import config


class S3Service:
    def __init__(self):
        key = config("AWS_ACCESS_KEY")
        secret = config("AWS_SECRET_KEY")
        region = config("S3_REGION")
        s3_bucket_name = config("S3_BUCKET_NAME")

        # object client through which we can control our s3 bucket/s
        self.client_s3 = boto3.client("s3", region_name=region, aws_access_key_id=key, aws_secret_access_key=secret)

