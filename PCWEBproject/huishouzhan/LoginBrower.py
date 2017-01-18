#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
profile=r'C:\Users\Administrator\AppData\Roaming\Mozilla\Firefox\Profiles\2e93sxcm.jzs'

class LoginBrower():
							#其他文件类里面的方法要直接调用下面的方法，必须设置此方法为静态方法；
	@staticmethod 			#如果是其他文件里类外面，直接调用此方法，则不需要设置静态，且此方法需加self。跟本身实例相关！
	def loginbr(url,user,password):
		try:
			FF=webdriver.Firefox()
			FF.maximize_window()
			FF.get(url)
			FF.find_element_by_xpath("//*[@id='loginId']").send_keys(user)
			FF.find_element_by_xpath("//*[@id='loginPwd']").send_keys(password)
			FF.find_element_by_xpath("//*[@id='btnLogin']").click()	
			return FF			
		except:
			print "login error"

										
	@staticmethod 			
	def loginkqc(url):
		# firefoxBin = os.path.abspath(r"D:\Mozilla Firefox\firefox.exe")
		# os.environ["webdriver.firefox.bin"] = firefoxBin
		try:
			#profileJ = webdriver.FirefoxProfile(profile)
			#firefoxdriver=r"D:\Mozilla Firefox\firefox.exe"
			#os.environ["webdriver.firefox.bin"]=firefoxdriver
			#profile1=webdriver.FirefoxProfile(profile)
			#打开指定浏览器
			global FF
			FF=webdriver.Firefox()
			FF.maximize_window()
			FF.get(url)		
			return FF			
		except:
			print "login error"

	@staticmethod 		
	def getAllhandle():
		allHandles=FF.window_handles
		return allHandles
	
	
	@staticmethod
	def closekqc(*driver):	
		try:
			for index in range(len(driver)):
				driver[index].close()

		except:
			print "close driver error"