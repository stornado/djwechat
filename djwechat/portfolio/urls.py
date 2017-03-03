#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-01-31 17:53:45
# @Author  : Ryan Stornado (ryan@zxytech.com)
# @Link    : https://github.com/stornado
# @Version : $Id$

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='portfolio-index'),
]
