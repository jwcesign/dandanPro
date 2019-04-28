# !/usr/bin/env python
# -*- coding:utf-8 -*-
from socket import *
from common import *
from mysql import *

def SendCodeBack(sock, client, data):
	data  =  str(data)
	sock.sendto(data.encode(), client)

def CheckUser(receive_data):
	data = receive_data.split('-')
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
	print(result)
	if (result[0]['passwd'] == str(passwd)):
		return data[2:], True
	else:
		return "", ReturnCode.ERR_USER

def VaildData(receive_data):
	if(receive_data != '' and '-' in receive_data):
		return True
	else:
		return False

def HandleDropCoin(sock, client, data):
	print("HandleDropCoin")
	print(data)
	if(len(data) == 4):
		machineCode = int(data[0])
		state = int(data[1])
		dropCoinNum = int(data[2])
		date = data[3]
	else:
		SendCodeBack(sock, client, ReturnCode.DATA_ERR)

def HandleMachineError(sock, client, data):
	print("HandleMachineError")
	print(data)
	if(len(data) == 3):
		machineCode = int(data[0])
		shopInfo = data[1]
		errorCode = data[2]
	else:
		SendCodeBack(sock, client, ReturnCode.DATA_ERR)

def HandleInventory(sock, client, data):
	print("HandleInventory")
	print(data)
	if(len(data) == 3):
		machineCode = int(data[0])
		inventorStat = int(data[1])
		machinePoster = data[2]
	else:
		SendCodeBack(sock, client, ReturnCode.DATA_ERR)

def HandleOutEgg(sock, client, data):
	print("HandleOutEgg")
	print(data)
	if(len(data) == 3):
		machineCode = int(data[0])
		outEggNum = int(data[1])
		date = data[2]
	else:
		SendCodeBack(sock, client, ReturnCode.DATA_ERR)

def HandleInEgg(sock, client, data):
	print("HandleInEgg")
	print(data)
	if(len(data) == 3):
		machineCode = int(data[0])
		inEggNum = int(data[1])
		date = data[2]
	else:
		SendCodeBack(sock, client, ReturnCode.DATA_ERR)

def HandleCoinBox(sock, client, data):
	print("HandleCoinBox")
	print(data)
	if(len(data) == 3):
		machineCode = int(data[0])
		date = data[1]
		state = int(data[2])
	else:
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
		OperationKind.COIN_BOX: HandleCoinBox
	}
	operationDic.get(kind, HandleWrongData)(sock, client, data)

def ReceiveHandleData(sk):
	while(True):
		receive_data, client = sk.recvfrom(1024)
		#这里的编码注意
		receive_data = receive_data.decode(encoding="utf-8")
		if(VaildData(receive_data)):
			data_without_user, user_ok = CheckUser(receive_data)
			if (user_ok == True):
				HandleDiffOperation(sk, client, data_without_user)
			else:
				SendCodeBack(sk, client, user_ok)
		else:
			SendCodeBack(sk, client, ReturnCode.DATA_ERR)
		

	