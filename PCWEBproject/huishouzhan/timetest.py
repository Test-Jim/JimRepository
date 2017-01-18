#!/usr/bin/python
# -*- coding: UTF-8 -*-
import time 
listtime=['0500','1800','2800','3800','4800','5800']

while True:
	timing=time.strftime("%M%S",time.localtime(time.time()))
	if timing in listtime:
		time.sleep(15)
		print "success" 

	else:
		pass