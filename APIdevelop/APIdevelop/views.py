#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'Test-Jin'
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
import datetime

def helloworld(request):
    return HttpResponse("Hello world")
# def current_datatime(request):
#     now=datetime.datetime.now()
#     t=get_template('current_datetime.html')
#     html=t.render(Context({'current_date':  now}))
#     return HttpResponse(html)
def current_datatime(request):
    now=datetime.datetime.now()
    return render_to_response('current_datetime.html',{'current_date':now})