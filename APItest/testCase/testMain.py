#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
from testCase.commonFunctions import commonFunctions,reWriteHtml
import unittest
import logging,sys

class testBegin(unittest.TestCase):

    #为什么使用setupclass而不使用setup？因为在接口跑之前，我们只需要初始化一次即可。
    @classmethod
    def setUpClass(self):
        self.baseurl=commonFunctions.commonfun.get_ini('url','baseurl')
        self.passmslist=[]
        self.errormslist=[]
        self.access_token=[]
        commonFunctions.commonfun.logPrint()
        self.headers=eval(commonFunctions.commonfun.get_ini('head','headers'))
    def test_A_login(self):
        '''登录login'''
        #0接口名称,1接口url,2接口方式,3登录与否,4k1,5v1,6k2,7v2……
        rowhandle=commonFunctions.commonfun.readExcel(line=1)
        logging.info('get excel data:'+commonFunctions.commonfun.printlist(rowhandle))
        #判断是否需要进行接口测试
        if rowhandle[0] != '':
            #进行接口测试
            response=commonFunctions.commonfun.post_or_get(rowhandle,self.baseurl,self.headers,access_token=None)
            ls = eval(response.text)
            logging.info(ls)
            #断言判断是否成功
            commonFunctions.commonfun.assertApi(ls,rowhandle[0])
            #获取接口时间
            if ls['code']==0:
                self.passmslist.append(commonFunctions.commonfun.getapitimes(response))
            else:
                self.errormslist.append(commonFunctions.commonfun.getapitimes(response))
            self.access_token.append(ls['data']['token'])
            #第二次断言
            logging.info('----------------------------------------------')
            self.assertEqual(ls['code'],0)

        else:
            pass
    def test_B_feedback(self):
        '''提交意见反馈'''
        rowhandle=commonFunctions.commonfun.readExcel(line=2)
        logging.info('get excel data:'+commonFunctions.commonfun.printlist(rowhandle))
        #判断是否需要进行接口测试
        if rowhandle[0] != '':
            #进行接口测试
            if rowhandle[3]==1:
                response=commonFunctions.commonfun.post_or_get(rowhandle,self.baseurl,self.headers,self.access_token[0])
            ls = eval(response.text)
            #断言判断是否成功
            commonFunctions.commonfun.assertApi(ls,rowhandle[0])
            #获取接口时间
            if ls['code']==0:
                self.passmslist.append(commonFunctions.commonfun.getapitimes(response))
            else:
                self.errormslist.append(commonFunctions.commonfun.getapitimes(response))
            #第二次断言
            logging.info('----------------------------------------------')
            self.assertEqual(ls['code'],0)

        else:
            pass
    def test_C_userInfo(self):
        '''用户资料'''
        rowhandle=commonFunctions.commonfun.readExcel(line=3)
        logging.info('get excel data:'+commonFunctions.commonfun.printlist(rowhandle))
        #判断是否需要进行接口测试
        if rowhandle[0] != '':
            #进行接口测试
            if rowhandle[3]==1:
                response=commonFunctions.commonfun.post_or_get(rowhandle,self.baseurl,self.headers,self.access_token[0])
            ls = eval(response.text)
            #断言判断是否成功
            commonFunctions.commonfun.assertApi(ls,rowhandle[0])
            #获取接口时间
            if ls['code']==0:
                self.passmslist.append(commonFunctions.commonfun.getapitimes(response))
            else:
                self.errormslist.append(commonFunctions.commonfun.getapitimes(response))
            #第二次断言
            logging.info('----------------------------------------------')
            self.assertEqual(ls['code'],0)

        else:
            pass
    def test_D_mobileVER(self):
        '''用户验证码验证'''
        rowhandle=commonFunctions.commonfun.readExcel(line=4)
        logging.info('get excel data:'+commonFunctions.commonfun.printlist(rowhandle))
        #判断是否需要进行接口测试
        if rowhandle[0] != '':
            #进行接口测试
            if rowhandle[3]==1:
                response=commonFunctions.commonfun.post_or_get(rowhandle,self.baseurl,self.headers,self.access_token[0])
            ls = eval(response.text)
            #断言判断是否成功
            commonFunctions.commonfun.assertApi(ls,rowhandle[0])
            #获取接口时间
            if ls['code']==0:
                self.passmslist.append(commonFunctions.commonfun.getapitimes(response))
            else:
                self.errormslist.append(commonFunctions.commonfun.getapitimes(response))
            #第二次断言
            logging.info('----------------------------------------------')
            self.assertEqual(ls['code'],0)

        else:
            pass


    @classmethod
    def tearDownClass(self):
        logging.info('mslist:'+str(self.passmslist))
        logging.info('errorlist:'+str(self.errormslist))


if __name__=='__main__':
    unittest.main()
