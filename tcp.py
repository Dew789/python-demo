import socket
import time

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('www.py4inf.com', 80))
mysocket.send(b'GET http://www.py4inf.com/cover.jpg HTTP/1.0\n\n')

count = 0

picture = b''
while True:
    data = mysocket.recv(5120)
    #if (len(data) < 1) : break
    time.sleep(0.25)
    count = count + len(data)
    print(len(data), count)
    picture = picture + data
mysocket.close()

head, pic = picture.split(b'\r\n\r\n', 1)

with open('stuff.jpg', 'wb') as e:
    e.write(pic)
