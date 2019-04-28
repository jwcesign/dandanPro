# !/usr/bin/env python
# -*- coding:utf-8 -*-
from socket import *

#创建udp conn
def CreateUdpConn(port, host):
	#运行多线程绑定同一个端口
	sk = socket(AF_INET, SOCK_DGRAM)
	sk.setsockopt(SOL_SOCKET, SO_REUSEPORT, 1)
	print(port)
	sk.bind((host, port))
	return sk