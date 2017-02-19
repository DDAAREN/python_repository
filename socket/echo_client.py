#!/usr/bin/env python
# _*_ coding: UTF-8 _*_

import socket
import sys

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost',8088))
    
    while True:
        data = raw_input("Please input something..\n")
        if not data:
            continue
        s.sendall(data)
        recv = s.recv(1024)
        if not recv: # 一定要判断是否有从server回来的数据，否则会一直卡在recv()过程
            continue
        print '[S]> ' + "\"" + recv + "\"" + '\n'
        if ('bye' in data) or ('shut' in data):
            break

    s.close()
    sys.exit(0)
