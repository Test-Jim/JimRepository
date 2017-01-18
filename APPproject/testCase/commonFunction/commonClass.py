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

	
	@staticmethod
	#填写购车人信息
	def info_from_buyer(driver):
		try:
			driver.find_element_by_id("co_customer_name").send_keys(u"测试")
			driver.find_element_by_id("co_customer_id").send_keys("330326199010101010")
			driver.find_element_by_id("co_customer_mobile").send_keys("15663333333")
		except Exception, e:
			logging.exception(e)

	@staticmethod
	#上传照片
	def	upload_pictures(driver):
		try:

			driver.switch_to_frame("iframe_upload_uidimg0")
			driver.find_element_by_id("tool_file_input").send_keys("C:\Users\Administrator.PC-201603070155\Desktop\pictures\p1.jpg")
			N=driver.current_window_handle
			driver.switch_to_window(N)
			time.sleep(1)
			driver.switch_to_frame("iframe_upload_uidimg1")
			driver.find_element_by_id("tool_file_input").send_keys("C:\Users\Administrator.PC-201603070155\Desktop\pictures\p2.png")
			time.sleep(0.2)
			return driver
		except Exception, e:
			logging.exception(e)

	@staticmethod
	#选择提车地址
	def get_car_address(driver):
		try:
			N=driver.current_window_handle
			driver.switch_to_window(N)			
			driver.find_element_by_css_selector("#order_form > div.desposit.address-menu > div > ul > li").click()
			driver.switch_to_frame("region_dialog")
			time.sleep(0.2)
			driver.find_element_by_css_selector("body > div > ul > li:nth-child(1)").click()
			time.sleep(0.2)
			driver.find_element_by_css_selector("body > div > ul > li:nth-child(2)").click()
			return driver
		except Exception, e:
			logging.exception(e)

	@staticmethod
	#在支付宝页面操作并支付
	def pay_into_alipay(driver):
		try:
			driver.find_element_by_id("J-acctname").send_keys("305540786@qq.com")
			driver.find_element_by_id("payPasswd_rsainput").send_keys("jzsalx@123")
			driver.find_element_by_id("submit-l").click()
			time.sleep(0.5)
			driver.find_element_by_css_selector("#main > div.tb-tradestatus.tb-tradestatus-action > table > tbody > tr > td > a.btn.btn-ok-s > span").click()
			time.sleep(0.5)
			driver.find_element_by_css_selector("#confirmPayment > span > input[type='submit']").click()
			time.sleep(3)
			driver.find_element_by_css_selector("#payPassword_container > div").send_keys("x")
			driver.find_element_by_id("J_authSubmit").click()
		except Exception, e:
			logging.exception(e)
