# -*- coding: utf-8 -*-
from django.http import Http404, HttpResponse
import datetime

def hello(request):
    x = u'Hello Word'
    return HttpResponse(x)

def main_page(request):
    main_html = '''<html><body><a href = "hello">Страница Hello Word</a></p>
     <a href = "datetime">Страница Дата и время</a></body></html>'''
    return  HttpResponse(main_html)

def current_datetime(request):
    today = datetime.datetime.today()
    html = '<html><body>Сейчас %s.</body></html>' % today
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except:
        raise Http404()
    dt = datetime.datetime.today() + datetime.timedelta(hours = offset)
    #assert False
    html  = "<html><body>Через %s часов будет %s.</body></html>" % (offset, dt)
    return HttpResponse(html)
