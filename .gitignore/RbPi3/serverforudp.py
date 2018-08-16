#UDP server code

import socket
#for udp -->SOCK_DGRAM
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

host='127.0.0.1'
port=12346

s.bind((host,port))

while True:
   data,addr=s.recvfrom(2048)
   print('got connection form ',addr)
   print(data)
   s.sendto(b'THank you client',addr)
   
