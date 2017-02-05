#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-10-09 16:40:41
# @Author  : Ryan Stornado (ryan@zxytech.com)
# @Link    : https://github.com/stronado
# @Version : $Id$

import time

from django.template.loader import render_to_string
from weixin.models import WeixinMP


class WechatEcho(object):

    def __init__(self, toUser, fromUser):
        self.toUser = toUser
        self.fromUser = fromUser
        self.createTime = int(time.time())

    def reply_text(self, content):
        return render_to_string('weixin/message/msg_text.xml',
                                context=dict(toUser=self.toUser,
                                             fromUser=self.fromUser,
                                             createTime=self.createTime,
                                             content=content))


class WechatMsgHandler(object):

    def handle_text(self, content):
        pass


class WechatEvtHandler(object):
    pass


class MPEchoServer(object):

    def __init__(self, appid):
        mp = WeixinMP.objects.get(appid=appid)
        self.app = mp
