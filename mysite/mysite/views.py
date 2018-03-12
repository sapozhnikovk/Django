# -*- coding: utf-8 -*-
from django.template.loader import get_template
#from django.template import Template, Context
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse
from random import random
import datetime


def hello(request):
    x = u'Hello Word'
    return HttpResponse(x)


def main_page(request):
    main_html = '''<html><body><a href = "hello">Страница Hello Word</a></p>
     <a href = "datetime">Страница Дата и время</a></body></html>'''
    return HttpResponse(main_html)

""" Неудобный метод
def current_datetime(request):
    today = datetime.datetime.today()
    t = get_template('current_datetime.html')
    #t = Template("<html><body>Сейчас {{ current_date }}.</body></html>")
    #html = t.render(Context({'current_date': today}))
    html = t.render({'current_date': today})
    return HttpResponse(html)"""
def current_datetime(request):
    x = random()
    current_date = datetime.datetime.today()
    #return render_to_response('current_datetime.html', {'current_date' : today,
    #                                                    'x': rannum})
    return render_to_response('current_datetime.html', locals())


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except:
        raise Http404()
    dt = datetime.datetime.today() + datetime.timedelta(hours=offset)
    # assert False
    return render_to_response('hours_ahead.html', locals())