#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-13 23:16:24
# @Author  : Ryan Stornado (ryan@zxytech.com)
# @Link    : https://github.com/stornado
# @Version : $Id$

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='wallpaper-index'),
    url(r'^next/$', views.next, name='wallpaper-next-page'),
    url(r'^search/$', views.search, name='wallpaper-search'),
]
