# !/usr/bin/env python
# -*- coding:utf-8 -*-
from udp_conn import *
from config import *
import time
from multi_thread import *

#主程序，整合其他代码
def main():
	CreateReceiveThread()
	while(True):
		time.sleep(1)
main()