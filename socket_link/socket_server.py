
# 需要打开两个命令行窗口，一个运行服务器程序，另一个运行客户端程序
# tcp

import socket
from threading import Thread

ss=socket.socket()
ss.bind(('127.0.0.1',8088))
ss.listen(5)


def run(conn):
    while True:
        try:
            data = conn.recv(1024)
            print(data)
            conn.send(data.upper())
        except Exception:
            break

if __name__ == '__main__':
    while True:
        print('等待客户端连接')
        conn,addr = ss.accept()
        print(f'客服端{addr}连接成功')
        # 创建新线程来处理TCP连接:
        t = Thread(target=run,args=(conn,))
        t.start()