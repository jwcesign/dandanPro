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
	        return result
	finally:
	    connection.close()

conn = ConnDataBase("localhost",
	                config.sql_user,
	                config.sql_passwd,
	                config.database)
result = ExcuteSql(conn, "select * from users where user_name='"+"jw"+"'")
print(result)