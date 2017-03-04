# -*- coding: utf-8 -*-
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_list_or_404
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _

from .models import Article
from .models import Author
from .models import Category
from .models import FeedChannel

from .parser import get_feed_channel
from .parser import update_articles

# Create your views here.


class Page:

    def __init__(self, **kw):
        self.title = kw.get('title')
        self.description = kw.get('description', '')
        self.keywords = kw.get('keywords', '')


def home(request):
    accessible_articles = get_list_or_404(Article, show=True)

    try:
        limit = request.GET.get('limit', request.POST.get('limit', 5))
        limit = int(limit)
    except:
        limit = 5
    paginator = Paginator(accessible_articles, limit)

    page = request.GET.get('page', request.POST.get('page', 1))
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    finally:
        rss_page = Page(title=_('FeedParser'))
        return render(request, 'rss/index.html',
                      {'articles': articles,
                       'page': rss_page})


def manifest(request):
    return JsonResponse({'name': 'FeedParser'})


def add_feed(request):
    url = request.POST.get('url', request.GET.get('url'))
    channel = get_feed_channel(url)
    if channel:
        return JsonResponse({'code': 200, 'message': 'add feed successed'})
    else:
        return JsonResponse({'code': 500, 'message': 'something unexpected happened'})


def update_feed(request):
    feeds = get_list_or_404(FeedChannel)
    add_num = 0
    for feed in feeds:
        add_num += update_articles(feed.link)
    return JsonResponse({'code': 200, 'message': '%d articles updated' % add_num})
