#UDP client

import socket

#for UDP --> SOCK_DGRAM

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.sendto(b'Hello world to server',('127.0.01',12346))
print(s.recvfrom(2048))
