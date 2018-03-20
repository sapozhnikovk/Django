# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import Book


#def search_form(request):
#    return render_to_response('search_form.html')

"""
def search(request):
    if 'q' in request.GET:
        message = 'Вы искали: %r' % request.GET['q']
    else:
        message = 'Вы отправили пустую форму'
    return HttpResponse(message)
"""
def search(request):
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
