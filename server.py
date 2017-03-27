import socket


server_address = ('localhost',5001)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(server_address)

sock.listen(1)

while True:
    connect, addr = sock.accept()
    print("Connection accepted from " + repr(addr[1]))

    req_string = connect.recv(1024)

    if req_string == 'Picture':

        connect.sendall('Here is your info')

        req_string = ''

        
    

    
    
    #print(connect.recv(1024))

c.close
