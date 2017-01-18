#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import urllib
import urllib2
import re
from bs4 import BeautifulSoup
import time
# f = open("C:\Users\Administrator.PC-201603070155\Desktop\JZS.txt", 'w+')
# interURL=['1','2','3','4']
# ALLlist=['1','2']
# extrlist=[]
# for index in range(len(interURL)):
#     if interURL[index] not in  ALLlist:
#         print interURL[index]
#         extrlist.append(interURL[index])
# print extrlist
        # for index in urlsList:                       
        #     try:
        #         request=urllib2.Request(index)  
        #         response=urllib2.urlopen(request)    
        #         if 'error messages' not in response.read():
        #             print "visite",index, 'success'
        #     except urllib2.URLError, e:
        #         if hasattr(e,"code"):
        #             print e.code,'visite',index,' fail'
       
        #如果当前页面的url都在 ALLurl里面,
a=1467359650
while(True):
    if a<int(time.time())<a+30:
        print a
        time.sleep(10)
        a=a+60
