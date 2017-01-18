#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.test import TestCase
import requests
import connetmysql
import re
from bs4 import BeautifulSoup
from selenium import webdriver
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
# Create your tests here.
def get_info():
    # if name==u'郎昊林':
    #     name=u'郎昊林'
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    data={'account':'jinzhangshuang','password':'26273b5e9eab8fd735c7ef8f47fce034','keepLogin[]':'on',
          'rederer':'http://project.kuaiqiangche.cc/index.php?m=company&f=browse'}
    s=requests.session()
    loginUrl='http://project.kuaiqiangche.cc/index.php?m=user&f=login'
    allUrl='http://project.kuaiqiangche.cc/index.php?m=report&f=bugcreate'
    login=s.post(url=loginUrl,data=data,headers=headers)
    response=s.get(url=allUrl,cookies = login.cookies,headers=headers)
    soup=BeautifulSoup(response.content,'lxml')

    worktimels,avgtimels,txtimels,csxlls,namels=[],[],[],[],[]

    driver=webdriver.PhantomJS()
    driver.get("http://project.kuaiqiangche.cc/index.php?m=report&f=setworktime")
    driver.implicitly_wait(30)
    driver.find_element_by_id('account').send_keys('jinzhangshuang')
    driver.implicitly_wait(30)
    driver.find_element_by_name('password').send_keys('jin@#123')
    driver.implicitly_wait(30)
    driver.find_element_by_id('submit').click()
    driver.implicitly_wait(30)
    driver.find_element_by_css_selector('#wrap > div > div.main > div > select > option:nth-child(27)').click()
    driver.implicitly_wait(30)
    driver.find_element_by_css_selector('#wrap > div > div.main > div > input.form-date.beg').click()
    driver.implicitly_wait(30)
    driver.find_element_by_css_selector('body > div:nth-child(4) > div.datetimepicker-days > table > thead > tr:nth-child(1) > th.prev > i').click()
    driver.find_element_by_css_selector('body > div:nth-child(4) > div.datetimepicker-days > table > thead > tr:nth-child(1) > th.prev > i').click()
    driver.implicitly_wait(30)
    driver.find_element_by_css_selector('body > div:nth-child(4) > div.datetimepicker-days > table > tbody > tr:nth-child(4) > td:nth-child(6)').click()



    driver.implicitly_wait(30)
    driver.find_element_by_css_selector('#wrap > div > div.main > div > button.btn.search').click()
    driver.implicitly_wait(30)

    for tester in soup.find_all(class_='a-center'):
        for data in tester.find_all('td')[10:11]:
            csxlls.append(data.get_text())


    name=driver.find_element_by_css_selector('#wrap > div > div.main > table > tbody > tr:nth-child(40) > td:nth-child(3) > a').text

    worktimels.append(driver.find_element_by_css_selector('#wrap > div > div.main > table > tbody > tr:nth-child(40) > td:nth-child(6)').text)
    avgtimels.append(driver.find_element_by_css_selector('#wrap > div > div.main > table > tbody > tr:nth-child(40) > td:nth-child(7)').text)
    txtimels.append(driver.find_element_by_css_selector('#wrap > div > div.main > table > tbody > tr:nth-child(40) > td:nth-child(8)').text)

    name=driver.find_element_by_css_selector('#wrap > div > div.main > table > tbody > tr:nth-child(21) > td:nth-child(3) > a').text

    worktimels.append(driver.find_element_by_css_selector('#wrap > div > div.main > table > tbody > tr:nth-child(21) > td:nth-child(6)').text)
    avgtimels.append(driver.find_element_by_css_selector('#wrap > div > div.main > table > tbody > tr:nth-child(21) > td:nth-child(7)').text)
    txtimels.append(driver.find_element_by_css_selector('#wrap > div > div.main > table > tbody > tr:nth-child(21) > td:nth-child(8)').text)

    name=driver.find_element_by_css_selector('#wrap > div > div.main > table > tbody > tr:nth-child(24) > td:nth-child(3) > a').text

    worktimels.append(driver.find_element_by_css_selector('#wrap > div > div.main > table > tbody > tr:nth-child(24) > td:nth-child(6)').text)
    avgtimels.append(driver.find_element_by_css_selector('#wrap > div > div.main > table > tbody > tr:nth-child(24) > td:nth-child(7)').text)
    txtimels.append(driver.find_element_by_css_selector('#wrap > div > div.main > table > tbody > tr:nth-child(24) > td:nth-child(8)').text)

    name=driver.find_element_by_css_selector('#wrap > div > div.main > table > tbody > tr:nth-child(43) > td:nth-child(3) > a').text

    worktimels.append(driver.find_element_by_css_selector('#wrap > div > div.main > table > tbody > tr:nth-child(43) > td:nth-child(6)').text)
    avgtimels.append(driver.find_element_by_css_selector('#wrap > div > div.main > table > tbody > tr:nth-child(43) > td:nth-child(7)').text)
    txtimels.append(driver.find_element_by_css_selector('#wrap > div > div.main > table > tbody > tr:nth-child(43) > td:nth-child(8)').text)

    name=driver.find_element_by_css_selector('#wrap > div > div.main > table > tbody > tr:nth-child(11) > td:nth-child(3) > a').text
    # print driver.page_source.decode('utf-8')
    worktimels.append(driver.find_element_by_css_selector('#wrap > div > div.main > table > tbody > tr:nth-child(11) > td:nth-child(6)').text)
    avgtimels.append(driver.find_element_by_css_selector('#wrap > div > div.main > table > tbody > tr:nth-child(11) > td:nth-child(7)').text)
    txtimels.append(driver.find_element_by_css_selector('#wrap > div > div.main > table > tbody > tr:nth-child(11) > td:nth-child(8)').text)
    #
    # for index in range(len(csxlls)):
    #     print worktimels[index],avgtimels[index],txtimels[index],csxlls[index],namels
    mobilels=['15868878686','18768112317','15168372561','18268252393','15669036110']

    handle,conn=connetmysql.Mysql.connet()
    connetmysql.Mysql.insert_testerwork(handle,worktimels,avgtimels,txtimels,csxlls,mobilels)
    connetmysql.Mysql.close(handle,conn)

def aa():
    handle,conn=connetmysql.Mysql.connet()
    connetmysql.Mysql.select_Name(handle)
    connetmysql.Mysql.select_testerwork(handle,name=u'张佳慧')
    connetmysql.Mysql.close(handle,conn)
if __name__=='__main__':
    get_info()