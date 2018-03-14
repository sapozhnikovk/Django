# -*- coding: utf-8 -*-
from django.template.loader import get_template
#from django.template import Template, Context
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse
from random import random
import datetime

def bootsrap(request):
    return render_to_response('bootstrap.html', locals())

def hello(request):
    x = u'Hello Word'

    f = open('mysite/dump.txt', 'r')
    dump_list = f.read()
    f.close()
    return render_to_response('hello.html', locals())

def main_page(request):
    return render_to_response('main.html', locals())

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

def display_meta(request):
    value = request.META.items()
    #value.sort()
    #html = []
    #for k, v in value:
     #   html.append((k, v))
    return render_to_response('meta.html', locals())

    #    html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    #return HttpResponse('<table>%s</table>' % '\n'.join(html))
