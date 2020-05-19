
# 需要打开两个命令行窗口，一个运行服务器程序，另一个运行客户端程序
# tcp

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