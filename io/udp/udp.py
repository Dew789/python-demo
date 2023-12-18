import time
import socket


def build_data():
    frame_start = bytes.fromhex("3355")                     # 2字节，上行数据开始
    device_type_code = bytes.fromhex("0c000000")            # 4字节
    head0 = bytes.fromhex("00")                             # 1字节
    head1 = bytes.fromhex("01")                             # 1字节
    head2 = bytes.fromhex("02")                             # 1字节
    body_include = bytes.fromhex("da")                      # 1字节
    length = 2000 * 2
    body_length = length.to_bytes(4, byteorder='big')       # body字段的总长度，4字节
    body = b""
    for i in range(2000):
        body += bytes.fromhex("aaaa")
    frame_end = bytes.fromhex("3355")                       # 2字节，上行数据结束

    data = b""
    data += frame_start
    data += device_type_code
    data += head0
    data += head1
    data += head2
    data += body_include
    data += body_length
    data += body
    data += frame_end

    return data


if __name__ == '__main__':
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Server address
    server_address = ('127.0.0.1', 18090)
    
    # Message to be sent
    data = build_data()
    count = 0
    should_end_time = time.time() + 1
    while True:
        count = count + 1
        sent = sock.sendto(data, server_address)
        if count == 20000:
            sleep_time = should_end_time - time.time()
            time.sleep(sleep_time if sleep_time > 0 else 0)

            count = 0
            should_end_time = time.time() + 1

            print("send timestamp: %s" % (time.time()))
