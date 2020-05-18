import socket
s = socket.socket()
s.connect(('127.0.0.1',8088))

while True:
    msg = input('>>>:').strip()
    if not msg:
        continue
    s.send(msg.encode('utf-8'))
    data = s.recv(1024)
    print(data.decode('utf-8'))