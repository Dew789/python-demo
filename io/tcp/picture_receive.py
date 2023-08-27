import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('www.py4inf.com', 80))
my_socket.send(b'GET http://www.py4inf.com/cover.jpg HTTP/1.0\n\n')

count = 0

picture = b''
while True:
    data = my_socket.recv(5120)
    if len(data) < 1:
        break

    count = count + len(data)
    print(len(data), count)
    picture = picture + data
my_socket.close()

head, pic = picture.split(b'\r\n\r\n', 1)

with open('stuff.jpg', 'wb') as e:
    e.write(pic)
