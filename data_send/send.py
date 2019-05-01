#!/usr/bin/python
# -*- coding: utf-8 -*-

from socket import *

client_socket = socket(AF_INET, SOCK_DGRAM)
max_times = 1
while True:
	msg = raw_input('Please input your data:')
	msg = msg.split(',')
	msg = '~'.join(msg)
	msg = str(msg)
	server_address = ("127.0.0.1", 3333)
	client_socket.sendto(msg, server_address)
	back_code, addr=client_socket.recvfrom(1024)
	print "back_code:", back_code
	if(int(back_code) == -2):
		for i in range(max_times):
			client_socket.sendto(msg, server_address)