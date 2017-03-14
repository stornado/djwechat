#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-14 11:34:56
# @Author  : Ryan Stornado (ryan@zxytech.com)
# @Link    : https://github.com/stronado
# @Version : $Id$

'''抓取爱壁纸资源'''

import multiprocessing
import requests

from django.core.management.base import BaseCommand
from django.core.management.base import CommandError

from wallpaper.models import Image
from wallpaper.models import Tag


def crawler(page):
    url = 'http://api.lovebizhi.com/android_v3.php?p={0}'.format(
        page)

    resp = requests.get(url)
    resp_json = resp.json()

    data = resp_json['data']

    crawled_num = 0
    for image in data:
        url = image['image']['big']
        tag_names = []
        for tag in image['tags']:
            tag_names.append(tag['name'])
        fileid = image['file_id']
        tag_names.reverse()
        title = tag_names.pop()

        tags = []
        for name in tags:
            tag, _ = Tag.objects.get_or_create(name=name)
            tags.append(tag)
        image, created = Image.objects.get_or_create(
            title=title, url=url, uuid=fileid)
        image.tags = tags
        if created:
            crawled_num += 1

    return crawled_num


class Command(BaseCommand):
    help = 'Crawling picture resources'

    def add_arguments(self, parser):
        parser.add_argument('pages', default=10, type=int)
        parser.add_argument('start', default=1, type=int)

    def handle(self, *args, **options):
        max_page_num = options['pages']
        start = options['start']
        pages = range(start, max_page_num)
        crawled_num = 0
        try:
            pool = multiprocessing.Pool()
            results = pool.map(crawler, pages)
            crawled_num = sum(results)
        except Exception as e:
            raise CommandError(e)
        self.stdout.write(self.style.SUCCESS(
            '%d images crawled' % crawled_num))
