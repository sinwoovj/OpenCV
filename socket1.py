from socket import *

host = '192.168.10.100'
port = 9999

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket .setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

server_socket.bind((host,port))

print('linsting...')
server_socket.listen()

client_socket, addr = server_socket.accept()

print('connected by', addr)

cnt = 0

while True:
    data = client_socket.recv(1024)

    if not data:
        break
    
    cnt += 1
    print(cnt, ':: received from', addr, data.decode())

    client_socket.sendall(data)

client_socket.close()
server_socket.close()