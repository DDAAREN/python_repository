#!/usr/bin/env python
# _*_ coding: UTF-8 _*_

import socket
import threading
import SocketServer
import time
import pdb


class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        cur_thread = threading.current_thread()
        response = "{0}: {1}".format(cur_thread.name, data)
        time.sleep(3)
        self.request.sendall(response)


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass


def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(message)
        response = sock.recv(1024)
        print "Received: {0}".format(response)
    finally:
        sock.close()


if __name__ == '__main__':
    HOST, PORT = "localhost", 0
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    #server = SocketServer.TCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address

    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    # 这个例子中，用threading.Thread的唯一作用是吧server线程放后台，
    # 然后可以进行其他操作，比如client请求
    # SocketServer.ThreadingMixIn的作用在于
    # 针对每个request的处理使用不同于主线程的其他线程

    print "Server loop running in thread:", server_thread.name

    client(ip, port, "Hello World 1")
    client(ip, port, "Hello World 2")
    client(ip, port, "Hello World 3")
    # 因为client()是按顺序调用
    # 此例子中并没有体现多线程并发的场景
    # 依然会按顺序依次创建子线程处理client请求

    server.shutdown()
