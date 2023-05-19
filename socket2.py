#client code
from socket import *

host = '192.168.10.100'
port = 9999

client_socket = socket(AF_INET, SOCK_STREAM)

client_socket.connect((host,port))
client_socket.sendall('안녕.'.encode())

data = client_socket.recv(1024)
print('received from', repr(data.decode()))

client_socket.close()