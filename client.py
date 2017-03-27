import socket

class Client:
    
    def __init__(self):
        server_address = ('localhost',5001)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(server_address)

    def request(self):
        print(sock.recv(1024))

    def close(self):
        sock.close



