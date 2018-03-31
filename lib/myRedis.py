#!/usr/bin/env python
# -*- coding:utf8 -*-
#
# Author: stone 
# Date: 2018-03-29

import json
import time
import redis
import math

def getRecord():
	r = redis.StrictRedis('localhost', 6379, 0)
	ret = r.blpop('shorturl_list', 60)
	
	if ret:
		value = ret[1]
		return value
	else:
		return False


def insertIntoHash(key, value):
	r = redis.StrictRedis('localhost', 6379, 0)

	flag = False
	if 1 == r.hexists('shorturl_hash', key):
		# TODO log
		return flag

	if 0 == r.hset('shorturl_hash', key, value):
		# TODO log
		pass
		
	return True


def removeFromHash(key):
	r = redis.StrictRedis('localhost', 6379, 0)
	
	if 0 == r.hdel('shorturl_hash', key):
		# TODO log	
		pass
		


def subscribe(threadId, comsumer):
	r = redis.StrictRedis('localhost', 6379, 0)
	p = r.pubsub()
	p.subscribe('shorturl_channel')
	for item in p.listen():
		if item['type'] == 'message':
			while True:
				record = getRecord()
				if record:
					dic = json.loads(record)
					timestamp = dic['time']
					rKey = "%d_%f" % (threadId, timestamp)

					if insertIntoHash(rKey, record):
						if comsumer(dic['key'], dic['url'], math.floor(timestamp)):
							removeFromHash(rKey)
				else:
					break
