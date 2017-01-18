#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import random
from selenium import webdriver
import smtplib  
from email.mime.multipart import MIMEMultipart  
from email.mime.text import MIMEText  
from email.mime.image import MIMEImage 
path="file:///D:/jmeter/apache-jmeter-2.11/kuaiqiangche/"
result_dir="D:\\jmeter\\apache-jmeter-2.11\\kuaiqiangche\\"
l=os.listdir(result_dir)
st = l.sort(key=lambda fn: os.path.getmtime(result_dir+"\\"+fn) if not os.path.isdir(result_dir+"\\"+fn) else 0)
htmlpath=path+l[-1]
htmlpath2=result_dir+l[-1]
driver=webdriver.Firefox()
driver.get(htmlpath)
failNumber=driver.find_element_by_css_selector("body > table:nth-child(5) > tbody > tr.Failure > td:nth-child(2)").text
driver.close()
if failNumber=='0':
	pass
else:
	sender = 'jinzhangshuang@kuaiqiangche.com'  
	receiver = 'jinzhangshuang@kuaiqiangche.com'  
	subject = 'API ERROR'  
	smtpserver = 'smtp.mxhichina.com'  
	username = 'jinzhangshuang@kuaiqiangche.com'  
	password = 'jzsalx@123'  
	  
	msgRoot = MIMEMultipart('related')  
	msgRoot['Subject'] = 'API ERROR number '+str(random.randint(0,999999))
	  
	#构造附件  
	att = MIMEText(open(htmlpath2, 'rb').read(), 'base64', 'utf-8')  
	att["Content-Type"] = 'application/octet-stream'  
	att["Content-Disposition"] = 'attachment; filename="APIgroup1.html"'  
	msgRoot.attach(att)  
	          
	smtp = smtplib.SMTP()  
	smtp.connect('smtp.mxhichina.com')  
	smtp.login(username, password)  
	smtp.sendmail(sender, receiver, msgRoot.as_string())  
	smtp.quit()	

