# !/usr/bin/env python
# -*- coding:utf-8 -*-
import pymysql as mdb
from config import *

def ConnDataBase(host, user, passwd, database):
	conn = mdb.Connect(host="localhost",
					   user=config.sql_user,
					   passwd=config.sql_passwd,
					   db=database,
					   charset='utf8mb4',
					   cursorclass=mdb.cursors.DictCursor)
	return conn

def ExcuteSql(connection, sql):
	try:
		with connection.cursor() as cursor:
			# Read a single record
			cursor.execute(sql)
			result = cursor.fetchall()
	finally:
		connection.commit()
		return result;