import socket


server_address = ('localhost',5001)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(server_address)

sock.listen(1)

while True:
    connect, addr = sock.accept()
    print("Connection accepted from " + repr(addr[1]))

    connect.sendall('Hello')

    print(connect.recv(1024))

c.close
