# !/usr/bin/env python
# -*- coding:utf-8 -*-

#状态码
class ReturnCode():
	OK = 0
	NO_RELATED_DATA = -1
	OPERATION_ERR = -2
	ERR_USER = -3
	DATA_ERR = -4

#操作类型
class OperationKind():
	DROP_COIN = 0
	MACHINE_ERR = 1
	INVENTORY = 2
	OUT_EGG = 3
	IN_EGG = 4
	COIN_MACHINE = 5

#操作状态码
#投币
class DropCoinCode():
	NORMAL = 0
	NOT_ENOUGH = -1
	SUPPLEMENT_ENOUGH = -2

#机器故障
class MachineErrorCode():
	NOT_OUT_EGG = -1
	OUT_EGG_HOLD = -2
	IN_EGG_HOLD = -3

#库存操作
class InventoryCode():
	INVENTORY_ENOUGH = 0
	INVENTORY_ZERO = -1
	LESS_LEVEL = -2