# !/usr/bin/env python
# -*- coding:utf-8 -*-
import _thread as thread
from config import *
from handle_data import *
from udp_conn import *

def CreateReceiveThread():
	for i in range(config.thread_num):
		sk=CreateUdpConn(config.conn_port, config.conn_ip)
		thread.start_new_thread(ReceiveHandleData, (sk,))
