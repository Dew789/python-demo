from minio import Minio

minio_client = Minio(endpoint='10.40.152.222:19000',
                     access_key='****',
                     secret_key='*********',
                     secure=False)

bucket_name = '*****'
policy = """
{
    "Statement": 
    [{"Action": 
    ["s3:GetBucketLocation", "s3:ListBucket"],
     "Effect": "Allow", "Principal": "*", "Resource": "arn:aws:s3:::%s"},
     {"Action": "s3:GetObject", "Effect": "Allow", "Principal": "*", "Resource": "arn:aws:s3:::%s/*"}
    ], 
    "Version": "2012-10-17"}
""" % (bucket_name, bucket_name)

if __name__ == "__main__":
    minio_client.set_bucket_policy(bucket_name, policy)

