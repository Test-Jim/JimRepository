#!/usr/bin/python
# -*- coding: UTF-8 -*-
from appium  import webdriver
import logging,time,os
#定义设备信息
desired_caps={}
desired_caps['device'] = 'android'
desired_caps['platformName']='Android'#使用哪种移动平台
#desired_caps['browserName']='Chrome'#移动浏览器名称,目前只能操作谷歌浏览器。
desired_caps['version']='5.0.1'#安卓版本
desired_caps['deviceName']='HUAWEI MT7-TL00'#这是测试机的型号，可以查看手机的关于本机选项获得
desired_caps['appPackage']='com.jeeinc.save.worry' #待测试的app的java package
#desired_caps['app'] = 'D:\\appium\\testapk\\dingding_178.apk'#被测试的App在电脑上的位置
desired_caps['appActivity']='com.jeeinc.save.worry.ui.ad.MainAdActivity' #待测试的app的Activity名字
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
temp=None
i=None
def testbegin():
	time.sleep(10)
	try:
		driver.find_element_by_id('com.jeeinc.save.worry:id/start_page_image').is_displayed()
		driver.swipe(718,1485,269,1485,500)
		time.sleep(0.2)
		driver.swipe(718,1485,269,1485,500)
		time.sleep(0.2)
		driver.swipe(718,1485,269,1485,500)
		time.sleep(0.2)
		driver.find_element_by_id('com.jeeinc.save.worry:id/iv_detail').click()
	except Exception, e:
		pass
	driver.tap([(321,1637),])
	# driver.find_elements_by_id('com.jeeinc.save.worry:id/imageView1')[3].click()
	# driver.implicitly_wait(30)
	# driver.find_element_by_id('com.jeeinc.save.worry:id/iv_header_no').click()
	# time.sleep(1)
	# driver.find_element_by_id('com.jeeinc.save.worry:id/bt_dialog_footer_ok').click()
	# driver.implicitly_wait(30)
	# driver.find_element_by_id('com.jeeinc.save.worry:id/username_input').send_keys('15669036110')
	# driver.find_element_by_id('com.jeeinc.save.worry:id/password_input').send_keys('qwe123')
	# driver.find_element_by_id('com.jeeinc.save.worry:id/login_btn').click()
	driver.implicitly_wait(30)
	driver.find_elements_by_id('com.jeeinc.save.worry:id/imageView1')[1].click()
	driver.implicitly_wait(30)
	driver.find_element_by_id('com.jeeinc.save.worry:id/header_left_button').click()
	driver.implicitly_wait(20)
	driver.find_element_by_xpath("//android.widget.TextView[@text='商家所在地区']").click()
	driver.implicitly_wait(20)
	driver.tap([(164,1551),])
	time.sleep(0.2)
	driver.swipe(533,1660,533,1452,1000)
	time.sleep(0.2)
	driver.swipe(533,1660,533,1452,1000)
	time.sleep(0.2)
	driver.swipe(533,1660,533,1452,1000)
	time.sleep(0.2)
	driver.swipe(533,1660,533,1452,1000)
	time.sleep(0.2)
	driver.swipe(533,1558,533,1452,1000)
	time.sleep(1)
	driver.find_element_by_id('com.jeeinc.save.worry:id/tv_ok').click()
	driver.find_element_by_id('com.jeeinc.save.worry:id/tv_filter_btn').click()
	driver.implicitly_wait(20)

	try:
		while True:						
			text=driver.find_elements_by_id('com.jeeinc.save.worry:id/tv_brand_series')
			for index in range(len(text)):

				temp=driver.find_elements_by_id('com.jeeinc.save.worry:id/tv_brand_series')[index].text
				print temp
				driver.find_elements_by_id('com.jeeinc.save.worry:id/tv_date')[index].click()
				driver.implicitly_wait(20)
				driver.find_element_by_id('com.jeeinc.save.worry:id/header_left_button').click()
				driver.implicitly_wait(20)
				if driver.find_elements_by_id('com.jeeinc.save.worry:id/tv_date')[index].text=='06-13':
					break
				else:
					pass

				i=index
			driver.swipe(537,1810,537,210,1500)
			time.sleep(1)
			print i
			if driver.find_elements_by_id('com.jeeinc.save.worry:id/tv_brand_series')[i].text==temp:
				driver.swipe(537,1810,537,210,1500)
			else:
				pass
			# try:
			# 	driver.find_element_by_xpath('//android.widget.TextView[@text="06-13"]').is_displayed()
			# 	break
			# except:
			# 	pass	
	except:
		pass	
if __name__ == '__main__':
	testbegin()
	os.popen("adb wait-for-device")
	os.popen("adb shell pm clear com.jeeinc.save.worry ")
