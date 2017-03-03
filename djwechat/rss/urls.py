#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-03 14:58:03
# @Author  : Ryan Stornado (ryan@zxytech.com)
# @Link    : https://github.com/stronado
# @Version : $Id$

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='rss-index'),
    url(r'^add/feed/$', views.add_feed, name='rss-add-feed'),
    url(r'^update/feed/$', views.update_feed, name='rss-update-feed'),
]
