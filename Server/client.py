import socket

server_address = ('localhost',5001)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(server_address)

while True:
    print(sock.recv(1024))
    
    

sock.close



