#!/usr/bin/python
# -*- coding: UTF-8 -*-
import xlrd
import logging
import time,os
import hashlib
import ConfigParser
import sys,requests
from reWriteHtml import strpath
reload(sys)
sys.setdefaultencoding( "utf-8" )

class commonfun():

    #获取接口时间
    @staticmethod
    def getapitimes(response):
        return str(response.elapsed.microseconds/1000)+'ms'

    #打印元组、列表、字典
    @staticmethod
    def printlist(array_list):
        str_ing=''
        if  'list' in str(type(array_list)):
            for index in array_list:
                str_ing=str_ing+str(index)+','
            return ('['+str_ing+']').replace(',]',']')

        if  'tuple' in str(type(array_list)):
            for index in array_list:
                str_ing=str_ing+index+','
            return ('('+str_ing+')').replace(',)',')')

        if  'dict' in  str(type(array_list)):
            for index in array_list:
                str_ing=str_ing+'"'+index+'":"'+str(array_list[index]).decode('unicode-escape')+'",'
            return '{'+str_ing+'}'

    #创建日志log
    @staticmethod
    def logPrint():

        path=strpath+'\logs\\'
        now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
        # filename=open(path+now,'w')
        logging.basicConfig(level=logging.INFO,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename=path+now+'.log',
                )

    @staticmethod
    def readExcel(line):
        excelHandle=xlrd.open_workbook(strpath+'\\api.xls')
        tableHandle=excelHandle.sheet_by_name('B2BAPI')
        #读列
        #colhandle=tableHandle.col_values(0)
        #读行
        colhandle=tableHandle.row_values(line)
        return colhandle
    @staticmethod
    def MD5_encr(str):
        m2 = hashlib.md5()
        m2.update(str)
        return m2.hexdigest()

    @staticmethod
    def get_ini(key1,key2):
        configHandle = ConfigParser.ConfigParser()

        configHandle.read(strpath+'\B2BAPI.ini')
        os.path.abspath('.')
        return configHandle.get(key1,key2)
    @staticmethod
    def post_or_get(rowhandle,baseurl,headers,access_token):
        commonfun.printlist(rowhandle)
        data={}
        #组装传入的data
        for index in range(4,len(rowhandle),2):
            data[rowhandle[index]]=str(rowhandle[index+1]).replace('.0','')
        if access_token!=None:
            data['access_token']=access_token
        #对密码进行MD5加密
        if data.has_key('password'):
            data['password']=commonfun.MD5_encr(data['password'])
        logging.info(commonfun.printlist(data))
        #获取url
        localurl=rowhandle[1]
        #使用不同方式进行接口传参
        if rowhandle[2]=='post':
            response=requests.post(baseurl+localurl,params=data,headers=headers)
        else:
            response=requests.get(baseurl+localurl,params=data,headers=headers)
        return response
    @staticmethod
    def assertApi(ls,str):
        #断言判断是否成功
        try:
            if ls['code']==0:
                logging.info(str+' success!')
            else:
                logging.info(str+' faild!')
        except Exception,e:
            logging.exception(e)
        finally:
            logging.info(commonfun.printlist(ls))

