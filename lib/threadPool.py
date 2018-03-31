#!/usr/bin/env python
# -*- coding:utf8 -*-
#
# Author: stone 
# Date: 2018-03-29

import os
import sys
import threading

import myRedis

curDir = os.path.dirname(__file__)
parDir = os.path.abspath(os.path.join(curDir, os.pardir))
sys.path.append(parDir)

from app.mysql import insertIntoMysql

threadNum = 5

class myThread(threading.Thread):
	def __init__(self, threadID):
		threading.Thread.__init__(self)
		self.threadID = threadID

	def run(self):
		myRedis.subscribe(self.threadID, insertIntoMysql)


class threadPool():
	def __init__(self):
		self.threadNum = threadNum
		self.threads = []
		
		for i in range (0, self.threadNum):
			thread = myThread(i)
			self.threads.append(thread)


	def run(self):
		for t in self.threads:
			t.start()
	

	def join(self):
		for t in self.threads:
			t.join()
