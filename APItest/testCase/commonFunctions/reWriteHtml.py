#!/usr/bin/python
# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import os,sys
import urllib2,logging,time
strpath=str(os.path.abspath('.'))


def reWriteApiReport(listms):
    result_dir="C:\Users\Administrator.PC-201603070155\PycharmProjects\APItest\html\\"
    l=os.listdir(result_dir)
    l.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn) if not os.path.isdir(result_dir+"\\"+fn) else 0)
    htmlpath=result_dir+l[-1]
    print htmlpath
    time.sleep(10)
    fp = open(htmlpath,'r+')
    soup=BeautifulSoup(fp,'lxml')
    listclass=soup.find_all(colspan='5')

    for index in range(len(listclass)):
        if listclass[index].string=='pass':
            listclass[index].string='pass'+'['+str(listms[index])+']'
        if listclass[index].string=='error':
            listclass[index].string='error'+'['+str(listms[index])+']'
        if listclass[index].string=='fail':
            listclass[index].string='fail'+'['+str(listms[index])+']'
    #移动到文件头,目的是为了下次依旧可以从文件头开始操作文件
    fp.seek(0,os.SEEK_SET)
    #重写整个文件
    fp.write(str(soup))
    fp.close()
