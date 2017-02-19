#!/usr/bin/env python
# _*_ coding: UTF-8 _*_

import socket
import time
import errno
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost',8088))
s.listen(5)

while True:
    conn,addr = s.accept() 
    # conn is a new socket object usable to send and receive data on the connection
    # and address is the address bound to the socket on the other end of the connection
    print 'Connected by', addr
    while True:
        try:
            data=conn.recv(1024)
            if 'bye' in data:
                conn.sendall('Bye too..')
                break
            if 'shut' in data:
                conn.sendall('I will shut in 3 sec..')
                time.sleep(3)
                conn.close()
                sys.exit(1)
            print '[C]> ' + "\"" + data + "\""
            conn.sendall(data)
        except socket.error as e:
            if e.errno == errno.EPIPE:
                print '处理了一个 Broken pipe error'
                break
        
    conn.close()
