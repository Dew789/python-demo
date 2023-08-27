import time
import socket


def simulate_audio_send():
    sock_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_client.connect(("10.40.152.198", 18090))

    head_data = bytes.fromhex("FCFCFCFC")             # 大小4
    version = bytes.fromhex("00")                     # 大小1
    size = bytes.fromhex("00000831")                  # 大小4，发送数据包的大小
    timestamp = bytes.fromhex("FCFCFCFCFCFCFCFC")     # 大小8

    device_id = bytes.fromhex("cafe00000001")         # 大小6

    sample_rate = bytes.fromhex("bb80")               # 大小2，位置40
    depth = bytes.fromhex("10")                       # 大小1

    channel = bytes.fromhex("01")                     # 大小1，位置43
    with open(r"/usr/src/app/48k_16bit_sin.pcm", "rb") as e:
        audio = e.read(2048)
    crc = bytes.fromhex("b1fd")                       # 大小2
    end = bytes.fromhex("00")                         # 大小1

    data = b""
    data += head_data                                 # 4
    data += version                                   # 1
    data += size                                      # 4
    data += timestamp                                 # 8
    data += bytes.fromhex("000000000000")             # 占位符6      ,位置23
    data += device_id                                 # 6           ,位置29
    data += bytes.fromhex("0000000000000000000000")   # 占位符11
    data += sample_rate                               # 2
    data += depth                                     # 1            ,位置43
    data += channel                                   # 1
    data += audio                                     # 2048
    data += crc                                       # 2
    data += end                                       # 1

    while True:
        sock_client.sendall(data)
        print("Send data success, length： %s" % len(data))
        time.sleep(0.02)


if __name__ == "__main__":
    simulate_audio_send()
