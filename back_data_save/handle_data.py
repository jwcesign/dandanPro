# !/usr/bin/env python
# -*- coding:utf-8 -*-
from socket import *
from common import *
from mysql import *

def SendCodeBack(sock, client, data):
	data = str(data)
	print("+++"+data+"+++")
	sock.sendto(data.encode(), client)

def CheckUser(receive_data):
	data = receive_data.split('~')
	if(len(data) < 3):
		return ReturnCode.DATA_ERR
	user = str(data[0])
	passwd = str(data[1])
	# TODO:check user
	conn = ConnDataBase("localhost",
						config.sql_user,
						config.sql_passwd,
						config.database)
	result = ExcuteSql(conn, "select * from users where user_name="+"'"+user+"'")
	conn.close()
	if (str(result[0]['passwd']) == str(passwd)):
		return data[2:], True
	else:
		return "", ReturnCode.ERR_USER

def VaildData(receive_data):
	if(receive_data != '' and '~' in receive_data):
		return True
	else:
		return False

def HandleDropCoin(sock, client, data):
	print("HandleDropCoin")
	print(data)
	if(len(data) == 4):
		machineCode = data[0]
		state = data[1]
		dropCoinNum = data[2]
		date = data[3]
		conn = ConnDataBase("localhost",
							config.sql_user,
							config.sql_passwd,
							config.database)
		sql = "select * from egg_machine where egg_machine_id="+machineCode
		result = ExcuteSql(conn, sql)
		if (len(result) == 0):
			SendCodeBack(sock, client, ReturnCode.NO_RELATED_DATA)
			return
		sql = "insert into egg_coin_ac values (null, "+machineCode+", "+state+", "+dropCoinNum+", "+date+")"
		result = ExcuteSql(conn, sql)
		SendCodeBack(sock, client, ReturnCode.OK)
		conn.close()
	else:
		SendCodeBack(sock, client, ReturnCode.DATA_ERR)

def HandleMachineError(sock, client, data):
	print("HandleMachineError")
	print(data)
	if(len(data) == 3):
		machineCode = data[0]
		errorCode = data[1]
		date = data[2]
		conn = ConnDataBase("localhost",
							config.sql_user,
							config.sql_passwd,
							config.database)
		sql = "select * from egg_machine where egg_machine_id="+machineCode
		result = ExcuteSql(conn, sql)
		if (len(result) == 0):
			SendCodeBack(sock, client, ReturnCode.NO_RELATED_DATA)
			return
		sql = "select * from error_code_info where error_kind="+errorCode
		result = ExcuteSql(conn, sql)
		if (len(result) == 0):
			SendCodeBack(sock, client, ReturnCode.DATA_ERR)
			return
		sql = "update egg_machine set error_kind="+errorCode+", err_time="+date+" where egg_machine_id="+machineCode
		result = ExcuteSql(conn, sql)
		SendCodeBack(sock, client, ReturnCode.OK)
		conn.close()
	else:
		SendCodeBack(sock, client, ReturnCode.DATA_ERR)

def HandleInventory(sock, client, data):
	print("HandleInventory")
	print(data)
	if(len(data) == 2):
		machineCode = data[0]
		inventorStat = data[1]
		conn = ConnDataBase("localhost",
							config.sql_user,
							config.sql_passwd,
							config.database)
		sql = "select * from egg_machine where egg_machine_id="+machineCode
		result = ExcuteSql(conn, sql)
		if (len(result) == 0):
			SendCodeBack(sock, client, ReturnCode.NO_RELATED_DATA)
			return
		sql = "update egg_machine set inventory_state="+inventorStat
		result = ExcuteSql(conn, sql)
		SendCodeBack(sock, client, ReturnCode.OK)
	else:
		SendCodeBack(sock, client, ReturnCode.DATA_ERR)

def HandleOutEgg(sock, client, data):
	print("HandleOutEgg")
	print(data)
	if(len(data) == 3):
		machineCode = data[0]
		inEggNum = data[1]
		conn = ConnDataBase("localhost",
							config.sql_user,
							config.sql_passwd,
							config.database)
		sql = "select * from egg_machine where egg_machine_id="+machineCode
		result = ExcuteSql(conn, sql)
		if (len(result) == 0):
			SendCodeBack(sock, client, ReturnCode.NO_RELATED_DATA)
			return
		date = data[2]
		sql = "insert into egg_ac values (null,"+machineCode+", 3, "+inEggNum+", "+date+")"
		result = ExcuteSql(conn, sql)
		sql = "update egg_machine set eggs_num=eggs_num-"+inEggNum+" where egg_machine_id="+machineCode
		result = ExcuteSql(conn, sql)
		SendCodeBack(sock, client, ReturnCode.OK)
		conn.close()
	else:
		SendCodeBack(sock, client, ReturnCode.DATA_ERR)

def HandleInEgg(sock, client, data):
	print("HandleInEgg")
	print(data)
	if(len(data) == 3):
		machineCode = data[0]
		inEggNum = data[1]
		conn = ConnDataBase("localhost",
							config.sql_user,
							config.sql_passwd,
							config.database)
		sql = "select * from egg_machine where egg_machine_id="+machineCode
		result = ExcuteSql(conn, sql)
		if (len(result) == 0):
			SendCodeBack(sock, client, ReturnCode.NO_RELATED_DATA)
			return
		date = data[2]
		sql = "insert into egg_ac values (null,"+machineCode+", 4, "+inEggNum+", "+date+")"
		result = ExcuteSql(conn, sql)
		sql = "update egg_machine set eggs_num=eggs_num+"+inEggNum+" where egg_machine_id="+machineCode
		result = ExcuteSql(conn, sql)
		SendCodeBack(sock, client, ReturnCode.OK)
		conn.close()
	else:
		SendCodeBack(sock, client, ReturnCode.DATA_ERR)

def HandleCoinMachine(sock, client, data):
	print("HandleCoinMachine")
	print(data)
	machineCode = data[0]
	conn = ConnDataBase("localhost",
						config.sql_user,
						config.sql_passwd,
						config.database)
	#machine_id
	sql = "select * from coin_machine where machine_id="+machineCode
	result = ExcuteSql(conn, sql);
	if (len(result) == 0):
		SendCodeBack(sock, client, ReturnCode.NO_RELATED_DATA)
		return
	if (len(data) == 3):
		#钥匙操作
		keyState = data[1]
		time = data[2]
		#更新钥匙状态
		sql = "update coin_machine set key_state="+keyState+" where machine_id="+machineCode
		result = ExcuteSql(conn, sql);
		#记录钥匙数据
		sql = "insert into coin_machine_key_ac values (null, "+machineCode+", "+keyState+", '"+time+"')";
		result = ExcuteSql(conn, sql);
		conn.close()
		SendCodeBack(sock, client, ReturnCode.OK)
		return
	if (len(data) == 4):
		#进出币操作
		print("进出币操作")
		machineCode = data[0]
		operationKind = data[1]
		coinNum = data[2]
		time = data[3]
		sql = "insert into coin_machine_ac values (null, "+machineCode+", "+operationKind+", "+coinNum+", '"+time+"')"
		result = ExcuteSql(conn, sql);
		if (operationKind == '2'): #出币
			sql = "update coin_machine set coin_num=coin_num-"+coinNum+" where machine_id="+machineCode
			result = ExcuteSql(conn, sql)
		if (operationKind == '3'): #进币
			sql = "update coin_machine set coin_num=coin_num+"+coinNum+" where machine_id="+machineCode
			result = ExcuteSql(conn, sql)
		SendCodeBack(sock, client, ReturnCode.OK)
		return

	SendCodeBack(sock, client, ReturnCode.DATA_ERR)

def HandleWrongData(sock, client, data):
	SendCodeBack(sock, client, ReturnCode.DATA_ERR)

def HandleDiffOperation(sock, client, data_without_user):
	kind = int(data_without_user[0])
	data = data_without_user[1:]
	operationDic = {
		OperationKind.DROP_COIN: HandleDropCoin,
		OperationKind.MACHINE_ERR: HandleMachineError,
		OperationKind.INVENTORY: HandleInventory,
		OperationKind.OUT_EGG: HandleOutEgg,
		OperationKind.IN_EGG: HandleInEgg,
		OperationKind.COIN_MACHINE: HandleCoinMachine
	}
	operationDic.get(kind, HandleWrongData)(sock, client, data)

def ReceiveHandleData(sk):
	while(True):
		receive_data, client = sk.recvfrom(1024)
		#这里的编码注意
		receive_data = receive_data.decode(encoding="utf-8")
		if(VaildData(receive_data)):
			data_without_user, user_ok = CheckUser(receive_data)
			print(data_without_user, user_ok)
			if (user_ok == True):
				HandleDiffOperation(sk, client, data_without_user)
			else:
				SendCodeBack(sk, client, user_ok)
		else:
			SendCodeBack(sk, client, ReturnCode.DATA_ERR)