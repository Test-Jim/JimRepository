#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib,urllib2
import requests
import re
import math
import xlwt
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
data={'account':'jinzhangshuang','password':'26273b5e9eab8fd735c7ef8f47fce034','keepLogin[]':'on',
      'rederer':'http://project.kuaiqiangche.cc/index.php?m=company&f=browse'}

def all():
    s=requests.session()
    loginUrl='http://project.kuaiqiangche.cc/index.php?m=user&f=login'
    allUrl='http://project.kuaiqiangche.cc/index.php?m=bug&f=browse&productid=5&branch=0&browseType=all&param=0'
    pageUrl='http://project.kuaiqiangche.cc/index.php?m=bug&f=browse&productID=5&branch=0&browseType=all&param=0&orderBy=&recTotal=356&recPerPage=20&pageID='

    login=s.post(url=loginUrl,data=data,headers=headers)
    response=s.get(url=allUrl,cookies = login.cookies,headers=headers)
    parr=re.compile("共 <strong>(.*?)</strong>",re.S)
    numlist=re.findall(parr,response.content)
    num=int(math.ceil(int(numlist[0])/20))+2
    f=xlwt.Workbook(encoding = 'utf-8')
    sheet1=f.add_sheet(u'禅道问题汇总',cell_overwrite_ok=True)
    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.name = 'SimSun'    # 指定“宋体”
    style.font = font
    row0=['bug等级','确认状态','bug标题','bug作者','bug指派给','解决负责人','结果状态']
    alllist=[]
    for index in range(0,len(row0)):
        sheet1.write(0,index,row0[index],style)
    for index in range(1,num):
        # print pageUrl+str(index)+'&productid=5'
        response=s.get(url=pageUrl+str(index)+'&productid=5',cookies = login.cookies,headers=headers)
        parr=re.compile("class='pri.*?>(.*?)</span>.*?<span class='confir.*?'>(.*?)</span>.*?style='color: '>(.*?)</a>.*?<td class='bug-.*?<td>(.*?)</td>"
                        ".*?<td .*?>(.*?)</td>.*?<td>(.*?)</td>.*?<td>(.*?)</td>",re.S)
        endlist=re.findall(parr,response.content)
        alllist.extend(endlist)
    for index1 in range(len(alllist)):
            for index2 in range(0,7):
                if alllist[index1][5]=='':
                    sheet1.write(index1+1,index2,alllist[index1][index2],style)
                    sheet1.write(index1+1,4,'')
                    sheet1.write(index1+1,5,alllist[index1][4])
                else:
                    sheet1.write(index1+1,index2,alllist[index1][index2],style)

    f.save('chandao.xlsx')
        



if __name__=='__main__':
    all()