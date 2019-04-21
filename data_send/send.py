#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests

#url发送地址
send_url = "http://10.211.55.8/back_data_save/main.php"
user_name = "姜伟"
user_passwd = "12345678"

#模拟输入和发送数据
while (True):
	print "Please input your data:",
	data = raw_input()
	payload = {'user': user_name, 'passwd': user_passwd, 'data': data}
	res = requests.get(send_url, params=payload)
	print res.text
