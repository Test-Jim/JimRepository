#!/usr/bin/python
# -*- coding: UTF-8 -*-
from selenium import webdriver
import re,xlrd,xlwt,time
from selenium.webdriver.common.keys import Keys
from bs4 import  BeautifulSoup


import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
class bug_mouth(object):
    def __init__(self):
        self.driver=webdriver.PhantomJS()
        self.driver.get("http://project.kuaiqiangche.cc/index.php?m=bug&f=browse&productID=5&branch=0&browseType=bySearch&queryID=myQueryID")
        self.driver.maximize_window()
    def bug_mouth_spider(self):
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id('account').send_keys('jinzhangshuang')
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_name('password').send_keys('jin@#123')
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id('submit').click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_css_selector('#field1 > option:nth-child(29)').click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_css_selector('#operator1 > option:nth-child(4)').click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_css_selector('#value1').send_keys('2017-01-01')
        self.driver.implicitly_wait(30)
        #上面是条件1，下面是条件2
        self.driver.find_element_by_css_selector('#field4 > option:nth-child(29)').click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_css_selector('#operator4 > option:nth-child(5)').click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_css_selector('#value4').send_keys('2017-01-31')
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id('submit').click()
        self.driver.implicitly_wait(30)
        time.sleep(1)
        recels=[]
        pagenum=self.driver.find_element_by_css_selector('#bugList > tfoot > tr > td > div.text-right > div > strong:nth-child(3)').text
        pagenum=pagenum.split('/')[1]

        for i in range(int(pagenum)):
            page = self.driver.page_source
            parr=re.compile('style="color: ">.*?<td class="bug-.*?">.*?</td>.*?<td>.*?</td>\s*<td>.*?</td>\s*<td>(.*?)</td>\s*<td>.*?</td>',re.S)
            templist=re.findall(parr,str(page))
            for index in range(len(templist)):
                recels.append(templist[index])
            recels = list(set(recels))
            if i<int(pagenum)-1:
                self.driver.find_element_by_css_selector('#bugList > tfoot > tr > td > div.text-right > div > a:nth-child(6) > i').click()
                self.driver.implicitly_wait(30)
        recels.remove('yangfengbo')
        self.driver.find_element_by_css_selector('#searchmore > i').click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_css_selector('#field2 > option:nth-child(6)').click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_css_selector('#operator2 > option:nth-child(1)').click()
        self.driver.implicitly_wait(30)

        excel=r'C:\Users\Administrator.PC-201603070155\Desktop\bugCount\1mouthbug.xlsx'
        rb=xlwt.Workbook(encoding = 'utf-8')
        sheet1=rb.add_sheet(u'当月bug统计',cell_overwrite_ok=True)
        style = xlwt.XFStyle()
        font = xlwt.Font()
        font.name = 'SimSun'
        style.font = font
        row0=['姓名\等级','P1','P2','P3','P4','bug编号','总bug数','总扣分值']
        for index in range(0,len(row0)):
            sheet1.write(0,index,row0[index],style)
        for name in range(len(recels)):
            self.driver.find_element_by_css_selector('#value2_chosen > a').click()
            self.driver.implicitly_wait(30)
            if recels[name]=='':
                self.driver.find_element_by_css_selector('#value2_chosen > div > div > input[type="text"]').send_keys(u'空')
            else:
                self.driver.find_element_by_css_selector('#value2_chosen > div > div > input[type="text"]').send_keys(recels[name].decode('utf-8'))
            self.driver.implicitly_wait(30)
            self.driver.find_element_by_css_selector('#value2_chosen > div > div > input[type="text"]').send_keys(Keys.ENTER)
            self.driver.implicitly_wait(30)


            self.driver.find_element_by_css_selector('#field5 > option:nth-child(19)').click()
            self.driver.implicitly_wait(30)
            self.driver.find_element_by_css_selector('#operator5 > option:nth-child(1)').click()
            self.driver.implicitly_wait(30)
            self.driver.find_element_by_css_selector('#value5_chosen > a').click()
            self.driver.implicitly_wait(30)
            self.driver.find_element_by_css_selector('#value5_chosen > div > ul > li:nth-child(4)').click()
            self.driver.find_element_by_css_selector('#value5_chosen > div > div > input[type="text"]').send_keys(u'已解决')
            self.driver.implicitly_wait(30)
            self.driver.find_element_by_css_selector('#value5_chosen > div > div > input[type="text"]').send_keys(Keys.ENTER)
            self.driver.implicitly_wait(30)
            self.driver.find_element_by_css_selector('#submit').click()
            print recels[name]
            try:
                self.driver.find_element_by_css_selector('#bugList > tfoot > tr > td > div.text-right > div > strong:nth-child(3)').is_displayed()
                pagenum=self.driver.find_element_by_css_selector('#bugList > tfoot > tr > td > div.text-right > div > strong:nth-child(3)').text
                pagenum=pagenum.split('/')[1]
            except:
                pagenum=0
            print pagenum
            idls=''
            lv1,lv2,lv3,lv4=0,0,0,0
            for i in range(int(pagenum)):
                page = self.driver.page_source
                soup=BeautifulSoup(str(page),"html.parser")
                #bugID
                templist=soup.find_all('a',href=re.compile('m=bug&f=view&bugID='),style=None)
                for index in templist:
                    idls+=index.string+'、'
                #bug等级
                templist=soup.find_all('span',class_=re.compile('severity'))
                for index in templist:
                    if '1' in index.string:
                        lv1+=1
                    if '2' in index.string:
                        lv2+=1
                    if '3' in index.string:
                        lv3+=1
                    if '4' in index.string:
                        lv4+=1
                if i<int(pagenum)-1:
                    self.driver.find_element_by_css_selector('#bugList > tfoot > tr > td > div.text-right > div > a:nth-child(6) > i').click()
                    self.driver.implicitly_wait(30)
            sheet1.write(name+1,0,recels[name])
            sheet1.write(name+1,1,lv1)
            sheet1.write(name+1,2,lv2)
            sheet1.write(name+1,3,lv3)
            sheet1.write(name+1,4,lv4)
            sheet1.write(name+1,5,idls)
            sheet1.write(name+1,6,lv1+lv2+lv3+lv4)
            sheet1.write(name+1,7,-(5*lv1+2*lv2+1*lv3))

        rb.save(excel)
if __name__=='__main__':
    aa=bug_mouth()
    aa.bug_mouth_spider()