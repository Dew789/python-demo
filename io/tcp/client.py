import socket


def client():
    sock_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_client.connect(('localhost', 9999))
    sock_client.sendall("How are you")

    data = sock_client.recv(1024)
    print("Recv '%s'" % data)

    sock_client.close()


if __name__ == "__main__":
    client()
