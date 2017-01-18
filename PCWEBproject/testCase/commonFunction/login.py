#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
import logging
import time
import ConfigParser
ini=ConfigParser.ConfigParser()
ini.read('D:\sublimeText\sublime2\Sublime Text 2\PCWEBproject\python.ini')
mobile_number=ini.get('register','mobileNumber')
class login:	
	@staticmethod
	def loginkqc(selfdriver):
		try:
			driver=selfdriver
			driver.find_element_by_id("login-dialog-btn").click()
			driver.switch_to_frame('login-dialog')
			time.sleep(0.2)
			driver.find_element_by_id("user_mobile").send_keys(mobile_number)
			driver.find_element_by_id("user_verify").send_keys("1234")
			time.sleep(0.2)
			driver.find_element_by_css_selector("#form > p.submit-login > a").click()
			time.sleep(1)
			logging.info("login success")
			tuichu=driver.find_element_by_css_selector("body > div.top-index > div.calcul_top > div > div.login > div > div > a").text
			logging.info(tuichu)
			phone_number=driver.find_element_by_css_selector("body > div.top-index > div > div > div.login > div > a:nth-child(3)").text
			if phone_number=='156****6110':
				return driver
			else:
				logging.info("login not right")
			
		except Exception,e:
			logging.exception(e)
