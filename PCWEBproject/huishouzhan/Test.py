#!/usr/bin/python
# -*- coding: UTF-8 -*-
#7STWLVOJ4TTOV47P    oppor7 udid
# class Parent:        # 定义父类
#    parentAttr = 100
#    def __init__(self):
#       print "调用父类构造函数"

#    def parentMethod(self):
#       print '调用父类方法'

#    def setAttr(self, attr):
#       Parent.parentAttr = attr

#    def getAttr(self):
#       print "父类属性 :", Parent.parentAttr

# class Child(Parent): # 定义子类
#    def __init__(self):
#       print "调用子类构造方法"

#    def childMethod(self):
#       print '调用子类方法 child method'

# c = Child()          # 实例化子类
# c.childMethod()      # 调用子类的方法
# c.parentMethod()     # 调用父类方法
# c.setAttr(200)       # 再次调用父类的方法
# c.getAttr()          # 再次调用父类的方法

#实例不能直接访问私有变量，得调用类里的方法访问私有变量
# class JustCounter:
# 	__secretCount = 0  # 私有变量
# 	publicCount = 0    # 公开变量

# 	def count(self):
# 		self.__secretCount += 1
# 		self.publicCount += 1
# 		print self.__secretCount

# counter = JustCounter()
# counter.count()
# counter.count()
# print counter.publicCount
#print counter.__secretCount  # 报错，实例不能访问私有变量

#import re

#line = "Cats are smarter than dogs"

# matchObj = re.match( r'(.*) are (.*?) (.*) ', line, re.M|re.I)

# if matchObj:
#    print "matchObj.group() : ", matchObj.group()
#    print "matchObj.group(1) : ", matchObj.group(1)
#    print "matchObj.group(2) : ", matchObj.group(2)
#    #print "matchObj.group(3) : ", matchObj.group(3)
#    #print "matchObj.group(4) : ", matchObj.group(4)
# else: 
#    print "No match!!"
# import 

# phone = "2004-959-559 # This is Phone Number"

# # Delete Python-style comments
# num = re.sub(r'#.*$', "", phone)
# num = re.sub(r'\D', "", num)
# print "Phone Num : ", num

# def maBin():
#      print "Too low,ye scurvy dog!"
#      # ....
# if __name__ == '__main__':  #当前文件没有被其他文件调用，则会执行下面方法。其他文件无法调用这
# #							   个方法
# list=[4,6,2,7,8,1,9]
# length=len(list)
# while length>0:
# 	for index in range(len(list)-1):
# 		if list[index]>list[index+1]:
# 			list[index]=list[index]+list[index+1]
# 			list[index+1]=list[index]-list[index+1]
# 			list[index]=list[index]-list[index+1]
# 	length-=1
# print list
# def test(*driver):
# 	for index in range(len(driver)):
# 		print driver[index]
# jzs=test(1,2,3,4,5,6)
#调用其他文件里的方法，那个方法里可以使用driver=self.driver，而self.driver是本方法的初始化的变量
# import sys
# import traceback
# import logging

# logging.basicConfig(level=logging.INFO,
#                 format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
#                 datefmt='%a, %d %b %Y %H:%M:%S',
#                 filename='mytest.log',
#                 filemode='w')
# traceback_template = '''Traceback (most recent call last):
#  File "%(filename)s", line %(lineno)s, in %(name)s
# %(type)s: %(message)s\n'''
# # Skipping the "actual line" item
# # Also note: we don't walk all the way through the frame stack in this example
# # see hg.python.org/cpython/file/8dffb76faacc/Lib/traceback.py#l280
# # (Imagine if the 1/0, below, were replaced by a call to test() which did 1/0.)
# try:
# 	1/0
# except:
# #http://docs.python.org/2/library/sys.html#sys.exc_info
# 	exc_type, exc_value, exc_traceback = sys.exc_info() # most recent (if any) by default
# 	'''
#   Reason this _can_ be bad: If an (unhandled) exception happens AFTER this,
#   or if we do not delete the labels on (not much) older versions of Py, the
#   reference we created can linger.
#  
#   traceback.format_exc/print_exc do this very thing, BUT note this creates a
#   temp scope within the function.
# 	'''
# 	traceback_details = {
# 	'filename':exc_traceback.tb_frame.f_code.co_filename,
# 	'lineno':exc_traceback.tb_lineno,
# 	'name':exc_traceback.tb_frame.f_code.co_name,
# 	'type':exc_type.__name__,
# 	'message':exc_value.message, # or see traceback._some_str()
# 	}
# 	del(exc_type, exc_value, exc_traceback) # So we don't leave our local labels/objects dangling
# 	#This still isn't "completely safe", though!
# 	# "Best (recommended) practice: replace all exc_type, exc_value, exc_traceback
# 	# with sys.exc_info()[0], sys.exc_info()[1], sys.exc_info()[2]
# 	## 修改这里就可以把traceback打到任意地方，或者存储到文件中了
# 	print traceback_template % traceback_details
import unittest,time,re
from selenium import webdriver
from commonClass import commonClass
class test():
	def fff(self):
		driver=webdriver.Firefox()
		driver.get("http://www.kuaiqiangche.com/")
		driver.find_element_by_css_selector("body > div.index-main-box > div.banner-brand > div > ul > li:nth-child(7) > a:nth-child(1)").click()
		time.sleep(1)
				
		nowhandle_1=driver.current_window_handle
		all_handle=driver.window_handles
		newhandle=commonClass.changeHandle(all_handle,nowhandle_1)
		print driver
				
		driver.switch_to_window(newhandle)
		driver.find_element_by_css_selector("#mainContent > div > ul > li:nth-child(1) > a > img").click()
		time.sleep(1)
		print driver.switch_to_window(newhandle)
				
		nowhandle_2=driver.current_window_handle
		all_handle=driver.window_handles
		newhandle=commonClass.changeHandle(all_handle,nowhandle_1,nowhandle_2)

		driver.switch_to_window(newhandle)
		driver.find_element_by_css_selector("#mainContent > div > div:nth-child(1) > div.left-img > a > img").click()
		time.sleep(3)
test().fff()