import socket

class Server:

    def __init__(self):
        server_address = ('localhost',5001)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(server_address)

    def request():
        print(sock.recv(1024))

    def close(self):
        sock.close



