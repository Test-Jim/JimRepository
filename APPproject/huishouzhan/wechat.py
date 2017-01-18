#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import time
import unittest
from selenium import webdriver
from appium  import webdriver
from lib2to3.pgen2.driver import Driver
from lib2to3.tests.support import driver
from selenium.common.exceptions import NoSuchElementException
import logging



desired_caps={}
desired_caps['device'] = 'android'
desired_caps['platformName']='Android'#使用哪种移动平台
#desired_caps['browserName']='Chrome'#移动浏览器名称,目前只能操作谷歌浏览器。
desired_caps['version']='4.4.2'#安卓版本
desired_caps['deviceName']='Android Emulator'#这是测试机的型号，可以查看手机的关于本机选项获得
desired_caps['appPackage']='com.alibaba.android.rimet' #待测试的app的java package
desired_caps['app'] = 'D:\\appium\\testapk\\dingding_178.apk'#被测试的App在电脑上的位置
desired_caps['appActivity']='com.alibaba.android.rimet.biz.SplashActivity' #待测试的app的Activity名字
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
 #如果知道被测试对象的apppage，appActivity可以加上下面这两个参数，如果不知道，可以注释掉，不影响用例执行
            
def tearDown():
    time.sleep(1)
    driver.quit()
    # os.popen("adb wait-for-device")
    # packageName=['com.kqc.user',"io.appium.unlock","io.appium.settings"]
    # for index in range(len(packageName)):
    #     os.popen("adb uninstall " + packageName[index]       

def test_wechat_add_friends():
    time.sleep(20)
    wechat_driver=driver

        #此处加上检测登录是否成功的代码
if __name__ == '__main__':
    test_wechat_add_friends()
    tearDown()