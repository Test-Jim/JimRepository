#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
import HTMLTestRunner
import time,threading
from testCase import AndroidAPP
def begin(pare):
    testunit=unittest.TestSuite()
    #将测试用例加入到测试容器(套件)中
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    if '1' in pare:
        testunit.addTest(unittest.makeSuite(AndroidAPP.LoginAndroidTests))
        filename = now+'result1.html'
    fp = file(filename, 'wb')

    runner =HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=pare,
        description=u'案例执行情况：')
    runner.run(testunit)
threads = []
t1 = threading.Thread(target=begin,args=("1",))
# t2 = threading.Thread(target=begin,args=("2",))
threads.append(t1)
# threads.append(t2)
if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()

