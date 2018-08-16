#TVP Server

import socket   #import socket package
#defining the socket for TCP communication
#TCP --> SOCK_STREAM
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host='127.0.0.1'         #defining an addres of server to which cliwnets can connect
port=12345              #using a port for our TCP server
s.bind((host,port))     #binding the address to the seocket

s.listen(5)             #make the server listen to the request
while True:
   ts,addr=s.accept()
   #accepting the client's request and creating a temporary socket  for the client
   print("got connection from client ",addr)
   ts.send(b"hello from TCP server")       #Sending data to the client
   ts.close()                             #cloisng the temproary socket

   
