#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
import tests
import requests
import re
import connetmysql

from bs4 import BeautifulSoup
# Create your views here.
def search_form(request):
    return render_to_response('search_form.html')
def get_tester_info(request):
    name=request.GET['name']
    handle,conn=connetmysql.Mysql.connet()
    tup=connetmysql.Mysql.select_testerwork(handle,name)
    print tup
    tup_2=connetmysql.Mysql.select_Name(handle)
    tup_2list=[]
    for index in tup_2:
        tup_2list.append(index[0])

    connetmysql.Mysql.close(handle,conn)

    if 'name' in request.GET:
        if name in tup_2list:
            message=u"{'code':'200','data':{'姓名':%s,'手机号':'%s','60天内月工作时长':'%s','当前可调休时长':'%s','日平均工作时长':'%s','60天内测试有效率':%s}}"%(name,tup[0][0],tup[0][1],tup[0][2],tup[0][3],tup[0][4])
        else:
            message="{'code':202,'message':'There is no such person'}"
        return HttpResponse(message)
    else:
        message='errorcode:300'
        return HttpResponse(message)


