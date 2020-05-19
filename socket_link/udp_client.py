#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 没有建立连接，直接发送数据包到IP地址和端口号

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)    # SOCK_DGRAM指定了这个Socket的类型是UDP

for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 8089))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))

s.close()