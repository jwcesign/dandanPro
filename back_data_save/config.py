# !/usr/bin/env python
# -*- coding:utf-8 -*-

class Config:
	def __init__(self,port,
		         ip, thread_num,
		         mysql_user, mysql_passwd,
		         database):
		self.conn_port = port
		self.conn_ip = ip
		self.sql_user = mysql_user
		self.sql_passwd = mysql_passwd 
		self.thread_num = thread_num
		self.database = database

config=Config(3333, "127.0.0.1", 3, "root", "root", "inventory_management")