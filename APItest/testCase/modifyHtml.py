#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
from bs4 import BeautifulSoup
import re,time

def readlogs():
    result_dir=os.path.abspath('..')+"\logs\\"
    l=os.listdir(result_dir)
    l.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn) if not os.path.isdir(result_dir+"\\"+fn) else 0)
    logpath=result_dir+l[-1]
    all_text=open(logpath,'r').read()
    pattern_one=re.compile('mslist:\[(.*?)\]',re.S)
    passmslist=re.findall(pattern_one,all_text)
    listpassms=passmslist[0].replace("'","").replace(" ",'').split(',')
    pattern_two=re.compile('errorlist:\[(.*?)\]',re.S)
    errormslist=re.findall(pattern_two,all_text)
    listerrorms=errormslist[0].replace("'","").replace(" ",'').split(',')
    return listpassms,listerrorms
    # target_list = [ x for x in mslist[0].replace("'",'').split(',')]
    # for index in target_list:
    #     print index
def modify(passmslist,errormslist):
    result_dir=os.path.abspath('..')+"\html\\"
    l=os.listdir(result_dir)
    l.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn) if not os.path.isdir(result_dir+"\\"+fn) else 0)
    htmlpath=result_dir+l[-1]
    fp = open(htmlpath,'r+')
    soup=BeautifulSoup(fp,'lxml')
    listpass=soup.find_all(colspan='5',text=True)
    listerror=soup.find_all(class_='popup_link')
    for index in range(len(listpass)):
        if listpass[index].string=='pass':
            listpass[index].string='pass'+'['+str(passmslist[index])+']'
    for index in range(len(listerror)):
        if 'fail'in listerror[index].string:
            listerror[index].string='fail'+'['+str(errormslist[index])+']'
        if 'error'in listerror[index].string:
            listerror[index].string='error'+'['+str(errormslist[index])+']'

    fp.seek(0,os.SEEK_SET)#移动到文件头,目的是为了下次依旧可以从文件头开始操作文件
    fp.write(str(soup))#重写整个文件
    fp.close()

if __name__ == '__main__':
    time.sleep(1)
    passmslist,errormslist=readlogs()
    modify(passmslist=passmslist,errormslist=errormslist)

