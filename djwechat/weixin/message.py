#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2016-10-09 20:12:41
# @Author  : Ryan Stornado (ryan@zxytech.com)
# @Link    : https://github.com/stornado
# @Version : $Id$

import time

from django.template.loader import render_to_string


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

    def reply_image(self, media_id):
        return render_to_string('weixin/message/msg_image.xml',
                                context=dict(toUser=self.toUser,
                                             fromUser=self.fromUser,
                                             createTime=self.createTime,
                                             media_id=media_id))

    def reply_voice(self, media_id):
        return render_to_string('weixin/message/msg_voice.xml',
                                context=dict(toUser=self.toUser,
                                             fromUser=self.fromUser,
                                             createTime=self.createTime,
                                             media_id=media_id))

    def reply_video(self, media_id, title, description):
        return render_to_string('weixin/message/msg_image.xml',
                                context=dict(toUser=self.toUser,
                                             fromUser=self.fromUser,
                                             createTime=self.createTime,
                                             media_id=media_id,
                                             title=title,
                                             description=description))

    def reply_news(self, artiles):
        if not artiles or not isinstance(artiles, (list, tuple)):
            return self.reply_text('')
        return render_to_string('weixin/message/msg_news.xml',
                                context=dict(toUser=self.toUser,
                                             fromUser=self.fromUser,
                                             createTime=self.createTime,
                                             artiles=artiles))

    def reply_music(self, title, description, music_url, hq_music_url, media_id):
        return render_to_string('weixin/message/msg_music.xml',
                                context=dict(toUser=self.toUser,
                                             fromUser=self.fromUser,
                                             createTime=self.createTime,
                                             title=title,
                                             description=description,
                                             music_url=music_url,
                                             hq_music_url=hq_music_url,
                                             media_id=media_id))
