#!/usr/bin/python3

#import socket

import socket

# Creat socket Server  & stable connect for internetworking

TCPSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Bind the socket on 8000 port

TCPSocket.bind(("0.0.0.0", 8000))

#listen connection 

TCPSocket.listen()

#Accept the Client Connection
#Define client name = ClientWin
 
(ClientWin,(ip,port))=TCPSocket.accept()

# go to clent and run on terminal

#telnet serverip(192.168.80.129)  port(8000)

#send data to client

#ClientWin.send(b"I am Ajeet Kumar")

#Received data to client

#ClientWin.resv(2048)

#Close Client socket

#ClientWin.close()

#Close Server socket

#TCPSocket.close()
