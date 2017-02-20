#!/usr/bin/env python
# _*_ coding: UTF-8 _*_

import SocketServer 

# 普通处理模式
class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        # self.request相当于conn,addr=socket.accept()里面的conn
        print "{} wrote:".format(self.client_address[0])
        print self.data
        self.request.sendall(self.data.upper())

# 流(类文件)处理模式
class MyTCPHandler_2(SocketServer.StreamRequestHandler):
    def handle(self):
        self.data = self.rfile.readline().strip()
        # self.rfile也相当于conn,但是它将客户端连接的对象按file方式处理
        print "{} wrote:".format(self.client_address[0])
        print self.data
        self.wfile.write(self.data.upper())
        


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999
    server = SocketServer.TCPServer((HOST,PORT), MyTCPHandler)
    server.serve_forever()

