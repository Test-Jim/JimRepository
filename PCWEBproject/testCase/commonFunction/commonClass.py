#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
import logging
import time
class commonClass():
	
	@staticmethod	
	#传入参数：1、当前所有窗口句柄，2、当前所有已经知道的窗口id。返回一个未知的窗口id
	def changeHandle(all_handle,*driver):
		#print all_handle,driver
		try:
			for index in range(len(all_handle)):
				if all_handle[index] not in driver:
					return all_handle[index]
		except Exception, e:
			logging.exception(e)

	@staticmethod
	def get_Now_and_All_handles(driver):
		try:
			nowhandle=driver.current_window_handle
			all_handle=driver.window_handles
			return nowhandle,all_handle
		except Exception, e:
			logging.exception(e)

	

