import time
import json
import uuid

from rocketmq.client import Producer, Message
from concurrent.futures import ThreadPoolExecutor

"""
  wget https://github.com/apache/rocketmq-client-cpp/releases/download/2.0.0/rocketmq-client-cpp-2.0.0-centos7.x86_64.rpm
  sudo rpm -ivh rocketmq-client-cpp-2.0.0-centos7.x86_64.rpm
  find / -name librocketmq.so
  export LD_LIBRARY_PATH=/usr/lib/librocketmq.so:$LD_LIBRARY_PATH
  sudo ldconfig
  """
def send_message(url):
    producer = Producer("rocketMQ-test-group")
    producer.set_name_server_address(url)
    producer.start()

    body = {
        "deviceSn": "cafe00000001:1",
        "messageId": str(uuid.uuid4()),
        "msgTime": 1693065601916,
        "tcpData": {
            "bits": 16,
            "samplingRate": 48000,
            "size": 7488,
            "timeLen": 10,
            "url": "ark-media/gyzn-data/cafe00000001:1/1/20230827/20230827000001916.pcm"
        }
    }
    msg = Message("IOT_MINIO_ZHITING_TCP_DATA")
    msg.set_body(json.dumps(body))

    while True:
        result = producer.send_sync(msg)
        print(result)
        time.sleep(10)


def concurrent_send(url, count):
    pool = ThreadPoolExecutor(count)
    for i in range(1, count + 1):
        pool.submit(send_message, url)

    while True:
        time.sleep(10)


if __name__ == "__main__":
    concurrent_send("10.40.152.198:9876", 1)
