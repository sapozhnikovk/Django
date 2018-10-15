# -*- coding: utf-8 -*-
from django.template.loader import get_template
# from django.template import Template, Context
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse
from random import random, randint
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
    wordlist = [u'На улице солнце', u'Возможно сегодня среда', u'Вот это тест',
                u'Это мои тестовые рандомные фразы', u'Я пытаюсь изучить Джанго',
                u'На улице снег', u'test', u'Рандомный текст', u'Еще бы взять его из интернета']
    wordlist_rnd = wordlist[randint(0, len(wordlist) - 1)]
    return render_to_response('main.html', locals())


def current_datetime(request):
    x = random()
    current_date = datetime.datetime.today()
    # return render_to_response('current_datetime.html', {'current_date' : today,
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
    path = request.path
    cookies = request.COOKIES

    # value.sort()
    # html = []
    # for k, v in value:
    #   html.append((k, v))
    return render_to_response('meta.html', locals())

    #    html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    # return HttpResponse('<table>%s</table>' % '\n'.join(html))

def calc(request):
    a = 0
    b = 0
    oper = 0
    try:
        if 'a' in request.GET and request.GET['a']:
            a = int(request.GET['a'])
        if 'b' in request.GET and request.GET['b']:
            b = int(request.GET['b'])
        if 'oper' in request.GET and request.GET['oper']:
            oper = request.GET['oper']
            if oper == '+':
                c = str(a + b)
            elif oper == '-':
                c = str(a - b)
            elif oper == '/':
                c = str(a / b)
            elif oper == '*':
                c = str(a * b)
            else:
                c = 'Вы ввели ошибочные данные'
    except ZeroDivisionError:
        c = 'На ноль делить нельзя'
    except ValueError:
        c = 'Над введенными вами данными нельзя производить математические операции'
    return render_to_response('calc.html', locals())

def rss(request):
    #   error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            search_result = True
            books = Book.objects.filter(title__icontains=q)
            render_to_response('search_form.html', locals())
    return render_to_response('search_form.html', locals())
"""
def calc(request):
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        else:
            search_result = True
            books = Book.objects.filter(title__icontains=q)
            render_to_response('search_form.html', locals())
    return render_to_response('calc.html', locals())
"""