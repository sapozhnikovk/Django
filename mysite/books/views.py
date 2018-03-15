# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import Book


def search_form(request):
    return render_to_response('search_form.html')


def search(request):
    if 'q' in request.GET:
        message = 'Вы искали: %r' % request.GET['q']
    else:
        message = 'Вы отправили пустую форму'
    return HttpResponse(message)

#def search(request):
#    if 'q' in request.GET and request.GET['q']:
#        q = request.GET['q']
#        books = Book.object.filter(title__icontains-q)
#        return render_to_response('search_results.html', locals())
#    else:
#        return HttpResponse('Введите поисковый запрос')
