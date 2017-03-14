#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-04 20:58:14
# @Author  : Ryan Stornado (ryan@zxytech.com)
# @Link    : https://github.com/stornado
# @Version : $Id$

import multiprocessing

from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

from rss.models import FeedChannel
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

            links = []
            for feed_channel in feed_channels:
                links.append(feed_channel.link)

            try:
                pool = multiprocessing.Pool()
                results = pool.map(update_articles, links)
                updated_num = sum(results)
            except Exception as e:
                raise CommandError(e)

            self.stdout.write(self.style.SUCCESS(
                '%d articles updated' % updated_num))
