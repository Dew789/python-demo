import socket


def blocking_server():
    sock_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock_server.bind(('localhost', 9999))
    sock_server.listen(10)

    while True:
        conn, addr = sock_server.accept()

        data = conn.recv(1024)
        print("Receive '%s' form %s" % (data, addr))
        conn.sendall("Hello")

        conn.close()


if __name__ == "__main__":
    blocking_server()
