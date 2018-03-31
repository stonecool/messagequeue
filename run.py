#!/usr/bin/env python
# -*- coding:utf8 -*-
#
# Author: stone 
# Date: 2018-03-29

from lib.threadPool import threadPool

def main():
	p = threadPool()
	p.run()
	p.join()

if __name__ == '__main__':
	main()
