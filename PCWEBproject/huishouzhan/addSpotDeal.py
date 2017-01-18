#!/usr/bin/python
# -*- coding: UTF-8 -*-
# #import time
# try:
#    fh = open("C:\Users\Administrator\Desktop\ly.txt", "b")
#    fh.write("This is my test file for exception handling!!")
# except :
#    print "Error: can\'t find file or read data"
# else:
#    print "Written content in the file successfully"
#    fh.close()
# class Employee:
#    '所有员工的基类'
#    empCount = 0

#    def __init__(self, name, salary):
#       self.name = name
#       self.salary = salary
#       Employee.empCount += 1
   
#    def displayCount(self):
#      print "Total Employee %d" % Employee.empCount

#    def displayEmployee(self):
#       print "Name : ", self.name,  ", Salary: ", self.salary

# "创建 Employee 类的第一个对象"
# emp1 = Employee("Zara", 2000)
# "创建 Employee 类的第二个对象"
# emp2 = Employee("Manni", 5000)
# emp1.displayEmployee()
# emp2.displayEmployee()
# print "Total Employee %d" % Employee.empCount
import time
import logging 
from selenium import webdriver
from DbControl import DbControl
from LoginBrower import LoginBrower
from Deformat import Deformat

#配置logging
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='mytest.log',
                filemode='w')

#类外全局变量
url='http://192.168.10.170:8088/ecas/login/html/login.html'
user='jzs'
password='aaa111'
sql="select amount1 from pos_spotfolder where pairs_id='USDCNY'"
spot=0
DBaddress="192.168.10.181"
DBuser="root"
DBpassword="cmcs"
DBname="ctmsguzhi"
class Interfirefox():
	#构造url
	# def __init__(self,url):
	# 	#初始化时，登录浏览器
	# 	self.url = url
	# 	self.driver = webdriver.Firefox()
	# 	#self.time.sleep(1)
	# 	self.driver.maximize_window()
	# 	#self.time.sleep(1)
	# 	self.driver.get(url)
	# 	self.driver.find_element_by_xpath("//*[@id='loginId']").send_keys('jzs')
	# 	self.driver.find_element_by_xpath("//*[@id='loginPwd']").send_keys('aaa111')
	# 	self.driver.find_element_by_xpath("//*[@id='btnLogin']").click()	
	# 	print "login success！"	
		#print driver.title.encode("gb2312") #titel无需打印

	#定义类里的全局句柄变量
	
		#添加即期交易
	def addSpotdeal(self):
		#list_amount1=['1M','2M','3M','4M','5M']
		list_amount1=['1M']
		#创建浏览器句柄
		driver=LoginBrower.loginbr(url,user,password)
		global spot
		spot=driver				
		time.sleep(5)
		spot.find_element_by_xpath("/html/body/div[7]/div/div[2]/a/A").click()
		time.sleep(0.5)
		spot.find_element_by_xpath("//*[@id='_erajs_tree_2']").click()	
		time.sleep(2)
		#句柄切换到即期窗口
		spot.switch_to_frame("spotDealInput")
		try:
			for index in range(len(list_amount1)):
				logging.debug("begin to add a spotdeal ,amount1=",list_amount1[index]) 	
				#输入交易账户
				spot.find_element_by_xpath("/html/body/form/div/div/ul/li[2]/div/span/input").send_keys('folderJZS')
				time.sleep(0.2)	
				#输入交易对手
				spot.find_element_by_xpath("/html/body/form/div/div/ul[2]/li[2]/div/span/input").send_keys('CPTY_a')
				time.sleep(0.2)	
				#输入货币对
				spot.find_element_by_xpath("/html/body/form/div/div/ul[3]/li[2]/div/span/input").send_keys('USD/CNY')
				time.sleep(0.2)	
				#输入交易金额1
				spot.find_element_by_xpath("//*[@id='amount1']").send_keys(list_amount1[index])
				time.sleep(1)
				#点击新增按钮
				spot.find_element_by_xpath("//*[@id='addBtn']").click()
				time.sleep(1)
				#关闭按钮
				spot.find_element_by_xpath("/html/body/div[13]/div[2]/div[4]/a").click()
				#复制交易
				time.sleep(0.2)
				spot.find_element_by_xpath("/html/body/form/div/div/div/ul/li[3]/div[3]/span").click()
		except Exception, e:
			raise e	
		finally:
			logging.info("add spotDeals over!")
			#转移句柄，再关闭窗口
			spot.switch_to_window(spot.current_window_handle)
			time.sleep(0.2)
			spot.find_element_by_xpath("/html/body/div[8]/div/div[2]/a[2]").click() 			
			#spot.switch_to_window("spotDealInput")

			
		#获取即期头寸数据
	def getPosSpot(self):
		try:
			global spot
			if spot==0:
				#创建浏览器句柄
				driver=LoginBrower.loginbr(url,user,password)
				spot=driver
				time.sleep(5)
				spot.find_element_by_xpath("/html/body/div[7]/div/div[2]/a").click()
				time.sleep(0.2)
				spot.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/ul/li[2]/div/a").click()
				time.sleep(0.7)
				spot.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/div/div/ul/li/ul/li/div/span[4]").click()
				time.sleep(0.7)
				iframe=spot.find_element_by_xpath("/html/body/div[8]/div[2]").get_attribute('id')
				print iframe
				spot.switch_to_frame(iframe)
				amount_1=spot.find_element_by_xpath("//*[@id='datagrid-row-r2-2-0']/td[3]/div/p").text
				amount_1=Deformat.amountFormat(amount_1)
				print amount_1
			else:
				#打开头寸监控
				spot.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/div/div/div[2]/div/ul/li[2]/div/a").click()
				time.sleep(0.7)
				#打开货币对头寸监控
				spot.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[2]/div/div/div/div/div/div/div/div/ul/li/ul/li/div/span[4]").click()
				time.sleep(0.7)
				iframe=spot.find_element_by_xpath("/html/body/div[8]/div[2]").get_attribute('id')
				#打印动态的iframe
				print "动态的iframe：",iframe			
				spot.switch_to_frame(iframe)
				#获取金额1
				amount_1=spot.find_element_by_xpath("//*[@id='datagrid-row-r2-2-0']/td[3]/div/p").text
				#清除金额格式
				amount_1=Deformat.amountFormat(amount_1)
				amount_DB1=self.compare()
				if float(amount_1)==float(amount_DB1[0][0]):
					print "equal"
				else:
					print "not equal",amount_1,	 amount_DB1[0][0]
				#关闭头寸
				spot.switch_to.window(spot.current_window_handle)
				time.sleep(0.2)
				spot.find_element_by_xpath("/html/body/div[8]/div/div[2]/a[8]").click()
		except Exception, e:
			raise e
		

		#数据比较
	def compare(self):
		DBend=DbControl.MysqlControl(sql,DBaddress,DBuser,DBpassword,DBname)
		for index in range(len(DBend)):
			print DBend[index]
		return DBend

#对类进行实例化
jzs=Interfirefox()
#调用新增即期方法
jzs.addSpotdeal()
#获取即期头寸数据
jzs.getPosSpot()




