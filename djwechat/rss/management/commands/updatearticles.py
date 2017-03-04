#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-04 20:58:14
# @Author  : Ryan Stornado (ryan@zxytech.com)
# @Link    : https://github.com/stornado
# @Version : $Id$

from django.core.management.base import BaseCommand, CommandError

from rss.models import FeedChannel, Article
from rss.parser import update_articles


class Command(BaseCommand):
    help = 'Update the specified Feed articles'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        try:
            feed_channels = FeedChannel.objects.all()
        except FeedChannel.DoesNotExist:
            raise CommandError('Please add feed first')
        else:
            updated_num = 0
            for feed_channel in feed_channels:
                try:
                    updated = update_articles(feed_channel.link)
                except Exception as e:
                    raise CommandError(e)
                else:
                    updated_num += updated
            self.stdout.write(self.style.SUCCESS('%d articles updated' % updated_num))
