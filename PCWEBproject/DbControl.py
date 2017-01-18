#!/usr/bin/python
# -*- coding: UTF-8 -*-
import MySQLdb
class DbControl():
	@staticmethod
	def MysqlControl(sql,DBaddress,DBuser,DBpassword,DBname):

		db=MySQLdb.connect(DBaddress,DBuser,DBpassword,DBname)

		cursor = db.cursor()
		try:

			cursor.execute(sql)
			#返回的是元组！
			results = cursor.fetchall() 			
		except:
			print "Error: unable to fecth data"
		
		db.close()
		return results