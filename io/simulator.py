import time
import socket
from concurrent.futures import ThreadPoolExecutor


def simulate_audio_send(device_id_hex, audio_file):
    sock_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_client.connect(("10.40.152.198", 18090))

    head_data = bytes.fromhex("FCFCFCFC")             # 大小4
    version = bytes.fromhex("00")                     # 大小1
    size = bytes.fromhex("00000831")                  # 大小4，发送数据包的大小
    timestamp = bytes.fromhex("FCFCFCFCFCFCFCFC")     # 大小8

    device_id = bytes.fromhex(device_id_hex)          # 大小6

    sample_rate = bytes.fromhex("bb80")               # 大小2，位置40
    depth = bytes.fromhex("10")                       # 大小1

    channel = bytes.fromhex("01")                     # 大小1，位置43
    with open(audio_file, "rb") as e:
        audio = e.read(2048)
    crc = bytes.fromhex("b1fd")                       # 大小2
    end = bytes.fromhex("00")                         # 大小1

    data = b""
    data += head_data                                 # 4
    data += version                                   # 1
    data += size                                      # 4
    data += timestamp                                 # 8
    data += bytes.fromhex("000000000000")             # 占位符6       ,位置23
    data += device_id                                 # 6            ,位置29
    data += bytes.fromhex("0000000000000000000000")   # 占位符11
    data += sample_rate                               # 2
    data += depth                                     # 1            ,位置43
    data += channel                                   # 1
    data += audio                                     # 2048
    data += crc                                       # 2
    data += end                                       # 1

    while True:
        sock_client.sendall(data)
        print("Send data success, device_id: %s" % device_id)
        time.sleep(0.02)


def concurrent_audio_send(count):
    pool = ThreadPoolExecutor(count)
    for i in range(1, count + 1):
        print("cafe%08d" % i)
        pool.submit(simulate_audio_send, "cafe%08d" % i, r"/usr/src/app/48k_16bit_sin.pcm")


if __name__ == "__main__":
    concurrent_audio_send(10)
