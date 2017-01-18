#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import time
import unittest
from selenium import webdriver
from appium  import webdriver
from lib2to3.pgen2.driver import Driver
from lib2to3.tests.support import driver
 
PATH=lambda p:os.path.abspath(
os.path.join(os.path.dirname(__file__),p)                            
)
global driver
class LoginAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps={}
        desired_caps['device'] = 'android'
        desired_caps['platformName']='Android'#使用哪种移动平台
        #desired_caps['browserName']='Chrome'#移动浏览器名称
        desired_caps['version']='4.4.4'#安卓版本
        desired_caps['deviceName']='OPPO R7'#这是测试机的型号，可以查看手机的关于本机选项获得
        desired_caps['appPackage']='com.android.chrome' #待测试的app的java package
        desired_caps['app'] = PATH('D:\\appium\\testapk\\ChromeBrowser.pc6.apk')#被测试的App在电脑上的位置
        desired_caps['appActivity']='org.chromium.chrome.browser.ChromeTabbedActivity' #待测试的app的Activity名字
        self.driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
 
        #如果知道被测试对象的apppage，appActivity可以加上下面这两个参数，如果不知道，可以注释掉，不影响用例执行
        
      
       
    def tearDown(self):
        time.sleep(1)
        self.driver.quit()
        # os.popen("adb wait-for-device")
        # packageName=['com.kqc.user',"io.appium.unlock","io.appium.settings"]
        # for index in range(len(packageName)):
        #     os.popen("adb uninstall " + packageName[index])
        

    def test_login(self):
        time.sleep(6)
        #点击“注册登录”按钮
        APPdriver=self.driver
        APPdriver.get("http://www.kuaiqiangche.com/wap")
        APPdriver.find_element_by_css_selector("body > div.nav_header_inner.login > img").click()
        time.sleep(1)
        APPdriver.find_element_by_id("user_tel").send_keys("15669036110")
        APPdriver.find_element_by_id("user_scode").send_keys("1111")
        APPdriver.find_element_by_css_selector("#regin > div > ul > input").click()
        time.sleep(1)
        #点击宝马logo
        APPdriver.tap([(117,1358)],)
        time.sleep(5)
        APPdriver.find_element_by_id("1857").click()
        time.sleep(2)
        #选择宝马5系
        APPdriver.find_element_by_css_selector("body > div.list_wrap > div:nth-child(1)").click()
        #选择宝马5系2014款典雅型
        time.sleep(2)
        APPdriver.find_element_by_css_selector("body > div.seris_list > div:nth-child(1) > div.car_img > img").click()
        time.sleep(2)
        APPdriver.find_element_by_id("complete").click()
        #准备支付    
        time.sleep(2)
        APPdriver.find_element_by_css_selector("body > div.footer2 > span.pay.img_pay").click()

        #填写购买者信息
        time.sleep(3)
        APPdriver.find_element_by_id("realname").send_keys("ceshi")
        APPdriver.find_element_by_id("phoneno").send_keys("15669036110")
        APPdriver.find_element_by_id("cardno").send_keys("330326199010101010")
        #上传身份证
        time.sleep(2)
        APPdriver.find_element_by_id("choose_front")
        F=APPdriver.find_element_by_id("upload_front")
        F.send_keys(u"手机存储\Pictures\Screenshots\p1.jpg").perform()


        #此处加上检测登录是否成功的代码
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)