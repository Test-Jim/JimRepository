#!/usr/bin/python
# -*- coding: UTF-8 -*-
import unittest
import HTMLTestRunner
import time,threading
from testCase import Phone_2,Phone_1
def begin(pare):
    testunit=unittest.TestSuite()
    #将测试用例加入到测试容器(套件)中
    # now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    if '1' in pare:
        testunit.addTest(unittest.makeSuite(Phone_2.LoginAndroidTests))
        filename = 'result1.html'
        fp = file(filename, 'wb')
        runner =HTMLTestRunner.HTMLTestRunner(
            stream=fp,
            title=pare,
            description=u'案例执行情况：')
        runner.run(testunit)

    # if '2' in pare:
    #     testunit.addTest(unittest.makeSuite(Phone_2.LoginAndroidTests))
    #     filename = now+'result2.html'
    #     fp = file(filename, 'wb')
    #     runner =HTMLTestRunner.HTMLTestRunner(
    #         stream=fp,
    #         title=pare,
    #         description=u'案例执行情况：')
    #     runner.run(testunit)


threads = []
t1 = threading.Thread(target=begin,args=('1'))
# t2 = threading.Thread(target=begin,args=("2",))
threads.append(t1)
# threads.append(t2)
if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    for t in threads:
        t.join()

