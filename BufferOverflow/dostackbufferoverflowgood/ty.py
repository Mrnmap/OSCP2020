import struct
ptr_jmp_esp=0x080414C3
jmp_esp=struct.pack("<I", ptr_jmp_esp) 
print jmp_esp
