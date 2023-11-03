import os
from minio import Minio
from minio.error import S3Error

minio_client = Minio(endpoint='10.40.152.222:19000',
                     access_key='****',
                     secret_key='*********',
                     secure=False)


def set_policy(bucket_name):
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

    minio_client.set_bucket_policy(bucket_name, policy)


def download_folder(bucket_name, folder_path, local_path):
    """
    ###服务器安装minio客户端
    curl https://dl.min.io/client/mc/release/linux-amd64/mc \
      --create-dirs \
      -o $HOME/minio-binaries/mc

    chmod +x $HOME/minio-binaries/mc
    export PATH=$PATH:$HOME/minio-binaries/

    ###

    ## 设置连接minio服务 别名 为fengdian
    mc alias set fengdian http://fengdian-minio.gyznts.com  minioadmin huOS9erJnXts


    # 查看fengdian 下的桶 和 桶下文件
    mc ls fengdian/
    mc ls fengdian/ark-media/web

    # copy fengdian 下的ark-media 桶下的文件 到/opt/下 需要递归参数 --recursive
    mc cp  --recursive fengdian/ark-media/web  /opt/
    """

    """
    # 替换为你的MinIO服务器地址、访问密钥、密钥和桶名
    minio_server = "fengdian-minio.gyznts.com"
    access_key = "minioadmin"
    secret_key = "huOS9erJnXts"
    bucket_name = "ark-media"

    # 替换为你要下载的文件夹路径和本地存储路径
    folder_path = "zhiting/783017485108322304_904448987690960896/1/202309/"
    local_path = "/root/data"
    """
    if not os.path.exists(local_path):
        os.makedirs(local_path)

    for obj in minio_client.list_objects(bucket_name, prefix=folder_path):
        file_name = obj.object_name
        file_path = os.path.join(local_path, file_name)
        try:
            minio_client.fget_object(bucket_name, file_name, file_path)
            print(f"下载成功： {file_name}")
        except S3Error as e:
            print(f"下载失败： {file_name}, 错误： {e}")


if __name__ == "__main__":
    pass
