import boto3
from botocore.exceptions import ClientError
from decouple import config
from werkzeug.exceptions import InternalServerError


class S3Service:
    def __init__(self):
        key = config("AWS_ACCESS_KEY")
        secret = config("AWS_SECRET_KEY")
        self.region = config("S3_REGION")
        self.s3_bucket_name = config("S3_BUCKET_NAME")
        self.client_s3 = boto3.client(
            "s3",
            region_name=self.region,
            aws_access_key_id=key,
            aws_secret_access_key=secret,
        )

    def upload_cover(self, path, key):
        try:
            self.client_s3.upload_file(path, self.s3_bucket_name, key)
            return f"https://{self.s3_bucket_name}.s3.{self.region}.amazonaws.com/{key}"
        except ClientError as ex:
            raise InternalServerError("Not Available!")
