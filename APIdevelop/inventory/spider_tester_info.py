#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
import connetmysql
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time,datetime

testName=['']
mobilels=['']
worktime,avgtime,txtime,csxlls=[],[],[],[]
def get_info():
    driver=webdriver.PhantomJS()
    driver.get('http://project.kuaiqiangche.cc/index.php?m=user&f=login&referer=L2luZGV4LnBocD8=')
    driver.implicitly_wait(30)
    driver.execute_script("$('#account').attr('value','jinzhangshuang');"
                          "$(':password').attr('value','jin@#123');"
                          "$('#submit').click()")
    time.sleep(0.5)
    driver.execute_script("$('#mainmenu ul li:nth-child(6) a').append(\"<span id='jzs1'><span>\");$('#jzs1').click()")
    time.sleep(0.5)
    driver.execute_script("$('#modulemenu ul li:nth-child(6) a').append(\"<span id='jzs2'><span>\");$('#jzs2').click()")
    time.sleep(0.5)
    day=getdaytim()
    driver.execute_script("$('div.main div select').val('15149230');"
                          "$('.form-date:first').attr('value','"+day+"');")
    driver.find_element_by_css_selector('#wrap > div > div.main > div > button.btn.search').click()

    WebDriverWait(driver,10).until(lambda dr: dr.find_element_by_css_selector('#wrap '
    '> div > div.main > table > tbody > tr:nth-child(21) > td:nth-child(1)').is_displayed())

    for index in testName:
        htmlcontent=driver.execute_script("return $('tbody:first tr').filter(\":contains("+index+")\").html()")
        soup=BeautifulSoup(htmlcontent,"lxml")
        tdlist=soup.find_all('td')
        worktime.append(tdlist[5].get_text())
        avgtime.append(tdlist[6].get_text())
        txtime.append(tdlist[7].get_text())
    #---------割-------------------------------------------
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    data={'account':'jinzhangshuang','password':'26273b5e9eab8fd735c7ef8f47fce034','keepLogin[]':'on',
          'rederer':'http://project.kuaiqiangche.cc/index.php?m=company&f=browse'}
    s=requests.session()
    loginUrl='http://project.kuaiqiangche.cc/index.php?m=user&f=login'
    allUrl='http://project.kuaiqiangche.cc/index.php?m=report&f=bugcreate'
    login=s.post(url=loginUrl,data=data,headers=headers)
    response=s.get(url=allUrl,cookies = login.cookies,headers=headers)
    soup=BeautifulSoup(response.content,'lxml')

    for tester in soup.find_all(class_='a-center'):
        for data in tester.find_all('td')[10:11]:
            csxlls.append(data.get_text())


    handle,conn=connetmysql.Mysql.connet()
    connetmysql.Mysql.insert_testerwork(handle,worktime,avgtime,txtime,csxlls,mobilels)
    connetmysql.Mysql.close(handle,conn)

def getdaytim():
    now=datetime.datetime.now()
    delta=datetime.timedelta(days=60)
    n_days=now-delta
    return n_days.strftime('%Y-%m-%d')
    # currentday=time.strftime("%Y-%m-%d")
    # if currentday.split('-')[1] in '01':
    #     left=int(currentday.split('-')[0])-1
    #     return str(left)+'-'+'11'+'-'+currentday.split('-')[2]
    # elif currentday.split('-')[1] in '02':
    #     left=int(currentday.split('-')[0])-1
    #     return str(left)+'-'+'12'+'-'+currentday.split('-')[2]
    # else:
    #     mid=int(currentday.split('-')[1][1])-2
    #     return currentday.split('-')[0]+\
    #           '-0'+str(mid)+'-'\
    #           +currentday.split('-')[2]


    # driver.quit()
if __name__=='__main__':
    get_info()