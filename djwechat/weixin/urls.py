"""djwechat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
"""

from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from views import WechatCorpServer
from views import WechatMpServer


urlpatterns = [
    url(r'^mp/(?P<appid>\w+)/$',
        csrf_exempt(WechatMpServer.as_view()), name='mp_server'),
    url(r'^corp/(?P<corpid>\w+)/(?P<agentid>\d+)/$',
        csrf_exempt(WechatCorpServer.as_view()), name='corp_server'),
]
