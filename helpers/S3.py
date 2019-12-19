import os
import boto3

class S3:
    def __init__(self):
        self.s3 = s3 = boto3.client('s3',
            aws_access_key_id=os.environ.get('AWS_ACCESS_KEY', '')
            aws_secret_access_key=os.environ.get('AWS_SECRET_KEY', '') # シークレットアクセスキー
            region_name=os.environ.get('AWS_REGION', 'ap-northeast-1');
        )


    def push(self):
        pass

    def delete(self):
        pass
