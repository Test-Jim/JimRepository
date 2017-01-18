#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
import HTMLTestRunner
import time
from testCase.commonFunctions import reWriteHtml
from testCase import testMain


testunit=unittest.TestSuite()
#将测试用例加入到测试容器(套件)中
testunit.addTest(unittest.makeSuite(testMain.testBegin))

filename =reWriteHtml.strpath+ '\html\\'+time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))+'result.html'

fp = file(filename, 'wb')
runner =HTMLTestRunner.HTMLTestRunner(
	stream=fp,
	title=u'车源宝接口测试',
	description=u'测试案例执行情况：')
runner.run(testunit)
