#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-04 22:05:11
# @Author  : Ryan Stornado (ryan@zxytech.com)
# @Link    : https://github.com/stornado
# @Version : $Id$

from django.core.management.base import BaseCommand, CommandError

from rss.models import Articles


class Command(BaseCommand):
    help = 'delete the specified mount article to retain'

    def add_arguments(self, parser):
        parser.add_arguments('retention', default=100, type=int)

    def handle(self, *args, **options):
        try:
            retention = options['retention']
            articles = Article.objects.order_by(
                '-publishedAt', '-updatedAt')[:retention]
        except Articles.DoesNotExist:
            raise CommandError('Please add feed first')
        else:
            deleted_num = 0
            for article in articles:
                try:
                    deleted, _ article.delete()
                except Exception as e:
                    raise CommandError(e)
                else:
                    deleted_num += deleted
            self.stdout.write(self.style.SUCCESS(
                '%d articles deleted' % deleted_num))
