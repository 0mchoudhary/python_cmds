import boto3

S3=boto3.resource('s3')
def upload_to_bucket(s3,file_name,bucket_name,source_path):
    data = open(source_path,'rb')
    s3.Bucket(bucket_name).put_object(Key=file_name,Body=data)
    print("Sucessfully uploaded in S3")

bucket_name = "omchoudharyyy"
source_path = "/Users/omchoudhary/Learning/backup1.tar.gz"
file_name = "backup.tar.gz"

upload_to_bucket(S3,file_name,bucket_name,source_path)
