import socket

# 创建UDP套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定到本地地址和端口
server_address = ('localhost', 10000)
sock.bind(server_address)

# 要发送的数据
message = 'Hello, World!'

# 将数据转换为字节串
data = message.encode('utf-8')

# 发送数据
sock.sendto(data, server_address)

# 关闭套接字
sock.close()
