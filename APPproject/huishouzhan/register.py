#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import time
import unittest
from appium  import webdriver
from datetime import datetime,date

#7月1号晚上八点时间戳：1467374400  晚上8点到早上8点20：44400 。 早上8点20到晚上8点 42000
# dayOfWeek = datetime.now().weekday()
# weeklist=[0,1,2,3,4]
# sevenone=1467374400
class DDregister(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps['device'] = 'android'
        desired_caps['platformName']='Android'#使用哪种移动平台
        #desired_caps['browserName']='Chrome'#移动浏览器名称,目前只能操作谷歌浏览器。
        desired_caps['version']='5.1.1'#安卓版本
        desired_caps['deviceName']='HUAWEI MT7-TL00'#这是测试机的型号，可以查看手机的关于本机选项获得
        desired_caps['appPackage']='com.alibaba.android.rimet' #待测试的app的java package
        desired_caps['app'] = 'D:\\appium\\testapk\\com.alibaba.android.rimet.apk'#被测试的App在电脑上的位置
        desired_caps['appActivity']='com.alibaba.android.rimet.biz.SplashActivity' #待测试的app的Activity名字
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        #如果知道被测试对象的apppage，appActivity可以加上下面这两个参数，如果不知道，可以注释掉，不影响用例执行
        
      
       
    def tearDown(self):
        time.sleep(1)
        self.driver.quit()
        # os.popen("adb wait-for-device")
        # packageName=['com.kqc.user',"io.appium.unlock","io.appium.settings"]
        # for index in range(len(packageName)):
        #     os.popen("adb uninstall " + packageName[index])
        

    def test_register(self):
		# if dayOfWeek in weeklist:
		# 	while(True):
        #if(sevenone<int(time.time()<sevenone+10)):
        time.sleep(7)
        try:
            self.driver.find_element_by_id('com.alibaba.android.rimet:id/et_pwd_login').is_displayed()
        except:
            self.conti()
        else:
            self.driver.find_element_by_id('com.alibaba.android.rimet:id/et_pwd_login').send_keys('qwertyuiop')
            self.driver.implicitly_wait(30)          
            self.driver.find_element_by_id('com.alibaba.android.rimet:id/btn_next').click()
            self.conti()
    
    def conti(self):
            time.sleep(4)
            self.driver.find_elements_by_id('com.alibaba.android.rimet:id/home_bottom_tab_icon')[1].click()
            time.sleep(3)
            self.driver.tap([(400,1607)],)
            # self.driver.implicitly_wait(30)
            time.sleep(3)
            self.driver.tap([(547,1048)],)
            time.sleep(3)
            self.driver.tap([(409,870)],)
            time.sleep(6)
            self.driver.find_element_by_id('com.alibaba.android.rimet:id/back_icon').click()
            time.sleep(4)
            self.driver.find_element_by_id('com.alibaba.android.rimet:id/close_icon').click()
		
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(DDregister)
    unittest.TextTestRunner(verbosity=2).run(suite)