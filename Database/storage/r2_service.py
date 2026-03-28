import boto3
import os

s3 = boto3.client(
    "s3",
    endpoint_url="https://<account_id>.r2.cloudflarestorage.com",
    aws_access_key_id="YOUR_R2_KEY",
    aws_secret_access_key="YOUR_R2_SECRET"
)

BUCKET = "multiva"


def upload_file(file_path, key):
    s3.upload_file(file_path, BUCKET, key)

    return f"https://<your-public-url>/{key}"