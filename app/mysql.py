#!/usr/bin/env python
# -*- coding:utf8 -*-
#
# Author: stone 
# Date: 2018-03-30

import MySQLdb

def insertIntoMysql(key, value, time):
	sql = "INSERT INTO `t_shorturl`(`key`, `value`, `time`) VALUES('%s', '%s', %d)" % (key, value, time)
	
	db = MySQLdb.connect('localhost', 'root', '', 'shorturl')
	cursor = db.cursor()
	
	flag = False
	try:
		cursor.execute(sql)
		db.commit()
		flag = True
	except:
		db.rollback()
	
	db.close()
	
	return flag
