# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

urlpatterns = patterns('users.views',
    url(r'^$', 'index', name='index'),
)
