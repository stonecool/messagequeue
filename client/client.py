#!/usr/bin/env python
# -*- coding:utf8 -*-
#
# Author: stone 
# Date: 2018-03-30

import time
import json
import redis

def send():
	r = redis.StrictRedis('localhost', 6379, 0)

	for i in range(0, 10):
		key = "key_%d" % i
		url = "url_%d" % i
		dic = {'key': key, 'value': url, 'time': time.time()}
		print(dic)
		str = json.dumps(dic)
		ret = r.rpush('shorturl_list', str)

	r.publish('shorturl_channel', 'aa')

send()
