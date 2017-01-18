#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
from LoginBrower import LoginBrower
import ConfigParser
import time
import logging
from commonClass import commonClass
import sys
import traceback


logging.basicConfig(level=logging.INFO,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='mytest.log',
                filemode='w')
# import StringIO
# fp = StringIO.StringIO()
# traceback.print_stack(file = fp )
# message = fp.getvalue()

ini=ConfigParser.ConfigParser()
ini.read('python.ini')
url=ini.get("brower","url")
user=ini.get("brower","user")
password=ini.get("brower",'password')
mobile=ini.get('register','mobile')
#file1=open('mytest.log', 'w')

class fiddler:

	def register(self):
		try:
			global driver
			driver=LoginBrower.loginkqc(url)
			time.sleep(0.1)
			logging.info("登录到官网成功....")		
			driver.find_element_by_id("login-dialog-btn").click()
			#切换到登录窗口的iframe
			driver.switch_to_frame('login-dialog')
			time.sleep(0.2)
			logging.info('输入手机号进行注册....')
			driver.find_element_by_id('user_mobile').send_keys(mobile)
			time.sleep(0.1)		
			
			#让driver_1成为全局的首页句柄，成为备用
			global driver_1
			driver_1=driver
			
			#让nowhandle_1成为全局的首页句柄id
			global nowhandle_1
			nowhandle_1=driver_1.current_window_handle
		except Exception,e:
			logging.exception(e)
			#logging.critical(e, exc_info=1) 
			
	

	def buycar(self):
		driver.find_element_by_xpath('/html/body/div/div/div/i').click()
		logging.info("关闭注册页面成功....")
		#iframe切换到window
		driver.switch_to_window(nowhandle_1)
		time.sleep(0.2)
		driver_1.find_element_by_css_selector("body > div.index-main-box > div.banner-brand > div > ul > li:nth-child(7) > a:nth-child(1)").click()
		logging.info("进入福特卖车窗口成功....")
		
		#定义福特窗口句柄dirver_2
		global driver_2
		driver_2=driver_1
		
		
		#让nowhandle_2成为福特汽车首页的句柄
		allhandles=LoginBrower.getAllhandle()
		global nowhandle_2
		nowhandle_2=commonClass.changeHandle(allhandles,nowhandle_1)

		driver_2.switch_to_window(nowhandle_2)
		#选择jeep
		driver_2.find_element_by_css_selector("body > div.brand-box > div > div.brand-category > ul > li:nth-child(8) > div > a:nth-child(1)").click()
		time.sleep(0.2)
		logging.info("选择福特自由之光汽车...")
		driver_2.find_element_by_xpath("//*[@id='mainContent']/div/ul/li/a/div[1]").click()
		time.sleep(0.2)


		#allhandles=driver_2.window_handles
		allhandles=LoginBrower.getAllhandle()
		nowhandle_3=commonClass.changeHandle(allhandles,nowhandle_1,nowhandle_2)
		driver_2.switch_to_window(nowhandle_3)
		driver_2.find_element_by_css_selector("#mainContent > div > div > div.left-img > a > img").click()

		#关闭window
		LoginBrower.closekqc(driver_1,driver_2)
jzs=fiddler()
jzs.register()
jzs.buycar()

