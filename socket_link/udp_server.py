#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 没有建立连接，直接发送数据包

import socket

ss = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # SOCK_DGRAM指定了这个Socket的类型是UDP

# 绑定端口:
ss.bind(('127.0.0.1',8089))

print('Bind UDP on 8089...')


while True:
    # 接收数据:
    data, addr = ss.recvfrom(1024)  # 从socket接收数据
    print('Received from %s:%s.' % addr)
    reply = 'Hello, %s!' % data.decode('utf-8')
    ss.sendto(reply.encode('utf-8'), addr)      # str.encode(encoding='UTF-8',errors='strict')
