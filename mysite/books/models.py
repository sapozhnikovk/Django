# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30, verbose_name=u'название издательства')
    address = models.CharField(max_length=50, verbose_name=u'адрес')
    city = models.CharField(max_length=60, verbose_name=u'город')
    state_province = models.CharField(max_length=30, verbose_name=u'область')
    country = models.CharField(max_length=50, verbose_name=u'страна')
    website = models.URLField(verbose_name=u'Сайт')

    def __unicode__(self):
        return self.name
    class Meta:
        ordering = ['name']

class Author(models.Model):
    first_name = models.CharField(max_length=100, verbose_name=u'имя')
    last_name = models.CharField(max_length=40, verbose_name=u'фамилия')
    email = models.EmailField(blank=True, verbose_name='e-mail')

    def __unicode__(self):
        return u'%s, %s' % (self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name=u'название книги')
    author = models.ManyToManyField(Author, verbose_name=u'автор')
    publisher = models.ForeignKey(Publisher, verbose_name=u'Издательство')
    publication_date = models.DateField(null=True, blank=True, verbose_name=u'Дата публикации')

    def __unicode__(self):
        return  self.title