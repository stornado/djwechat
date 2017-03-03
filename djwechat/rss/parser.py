#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-03 17:22:38
# @Author  : Ryan Stornado (ryan@zxytech.com)
# @Link    : https://github.com/stronado
# @Version : $Id$

# 使用feedparser获取网源

import feedparser
import time

from datetime import datetime

from django.db import IntegrityError

from .models import Article
from .models import Author
from .models import Category
from .models import FeedChannel


def get_feed(url):
    feed = {}
    try:
        d = feedparser.parse(url)
        feed['title'] = d['feed']['title']
        feed['link'] = d['feed'].get('href', url)
        feed['website'] = d['feed'].get('link', '')
        feed['subtitle'] = d['feed'].get('subtitle', '')
        feed['description'] = d['feed'].get('description', '')
    finally:
        return feed


def struct_to_datetime(struct):
    return datetime.fromtimestamp(time.mktime(struct))


def timestamp_to_datetime(timestamp):
    return datetime.fromtimestamp(timestamp)


def datetime_to_string(datetime, fmt='%Y-%m-%d %H:%M:%S.%f'):
    '''YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]'''
    return datetime.strftime(fmt)


def get_articles(url):
    articles = []
    feed = feedparser.parse(url)
    channel = get_feed(url)
    for i, entry in enumerate(feed.entries, start=1):
        try:
            article = {}
            article['title'] = entry.get('title')
            article['link'] = entry.get('link')
            # authors = []
            # author['name'] = entry.get('author', '')
            # try:
            #     author['link'] = entry.get(
            #         'author_detail').get('href', '')
            # except AttributeError:
            #     author['link'] = ''
            # authors.append(author)
            authors = entry.get('authors', [])
            if not authors:
                authors = [
                    {'name': entry.get('author', entry.get('source', ''))}
                ]
            article['authors'] = authors
            categories = []
            category = entry.get('category', '')
            categories.append(category)
            article['categories'] = categories
            article['summary'] = entry.get('summary', '')
            content = entry.get('content', entry.get('description', ''))
            if isinstance(content, (list,)):
                try:
                    article['content'] = content[0]['value']
                except:
                    pass
            elif isinstance(content, (str,)):
                article['content'] = content

            article['published'] = datetime_to_string(struct_to_datetime(
                entry.get('published_parsed')))
            article['updated'] = datetime_to_string(struct_to_datetime(
                entry.get('updated_parsed')))

            article['guid'] = entry.get('id', entry.get('link'))
            articles.append(article)
        except IntegrityError:
            pass
    return articles


def get_feed_channel(url):
    channel = get_feed(url)
    feed_channel, _ = FeedChannel.objects.get_or_create(
        title=channel['title'],
        link=channel['link'],
        website=channel['website'],
        subtitle=channel['subtitle'],
        description=channel['description'])
    return feed_channel


def update_articles(url):
    add_num = 0
    articles = get_articles(url)
    feed_channel = get_feed_channel(url)
    for article in articles:
        try:
            authors = []
            for author in article['authors']:
                a, _ = Author.objects.get_or_create(
                    name=author.get('name', ''))
                authors.append(a)

            categories = []
            for category in article['categories']:
                c, _ = Category.objects.get_or_create(
                    tag=category)
                categories.append(c)

            saved_article = Article(
                channel=feed_channel,
                title=article['title'],
                link=article['link'],
                content=article['content'],
                publishedAt=article['published']
            )
            saved_article.save()
            saved_article.authors = authors
            saved_article.categories = categories
        except IntegrityError:
            pass
        else:
            add_num += 1
    return add_num
