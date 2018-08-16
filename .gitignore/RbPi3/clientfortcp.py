#client code for TCP

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#connecting to the TCP server with the address of
#the tcp server
s.connect(('127.0.0.1',12345))

print(s.recv(1024))
s.close()
