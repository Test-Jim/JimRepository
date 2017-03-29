#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import time
import unittest
from commonFunction import log_print
from appium  import webdriver
from lib2to3.pgen2.driver import Driver
from lib2to3.tests.support import driver
import logging
PATH=lambda p:os.path.abspath(
os.path.join(os.path.dirname(__file__),p)                            
)

class LoginAndroidTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        log_print.logPrint('androidtest_Phone_2.log')
        desired_caps={}
        desired_caps['device'] = 'android'
        desired_caps['platformName']='Android'#使用哪种移动平台
        #desired_caps['browserName']='Chrome'#移动浏览器名称
        desired_caps['version']='4.4.4'#安卓版本
        desired_caps['deviceName']='OPPO R7'#这是测试机的型号，可以查看手机的关于本机选项获得
        desired_caps['app'] = PATH('..\com.kqc.b2b_20.apk')
        #如果知道被测试对象的apppage，appActivity可以加上下面这两个参数，如果不知道，可以注释掉，不影响用例执行
        desired_caps['appPackage']='com.kqc.b2b' #待测试的app的java package
        desired_caps['appActivity']='com.kqc.b2b.ui.splash.SplashActivity' #待测试的app的Activity名字
        cls.driver=webdriver.Remote('http://localhost:4724/wd/hub',desired_caps)
        logging.info('begin')

    def test_login(self):
        time.sleep(5)
        try:
            self.driver.find_element_by_id('android:id/button1').is_displayed()
            self.driver.find_element_by_id('android:id/button1').click()
        except:
            pass
        self.driver.find_element_by_id('v_badge_view').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('tv_pwd_login').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('et_login_phone').send_keys('15669036110')
        self.driver.find_element_by_id('et_login_pwd').send_keys('qqqqqq')
        self.driver.find_element_by_id('tv_login_login').click()
        self.assertEqual('a','b')
        # APPdriver.tap([(529,1585),])

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        os.popen("adb wait-for-device")
        packageName=['com.kqc.b2b',"io.appium.unlock","io.appium.settings"]
        for index in range(len(packageName)):
            os.popen("adb uninstall " + packageName[index])
# if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(LoginAndroidTests)
    # unittest.TextTestRunner(verbosity=2).run(suite)