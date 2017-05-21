# -*- coding: utf-8 -*-
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_list_or_404
from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _

from .models import Image

# Create your views here.


def home(request):
    return render(request, 'wallpaper/index.html', {})


def next(request):
    return search(request)


def search(request):
    keyword = request.POST.get('keyword', '')
    if not keyword:
        all_images = get_list_or_404(Image, show=True)
    else:
        all_images = get_list_or_404(Image, show=True, title__icontains=keyword)
    try:
        limit = request.GET.get('limit', request.POST.get('limit', 5))
        limit = int(limit)
    except:
        limit = 5
    paginator = Paginator(all_images, limit)

    page = request.GET.get('page', request.POST.get('page', 1))
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        images = paginator.page(1)
    except EmptyPage:
        images = paginator.page(paginator.num_pages)
    finally:
        return render(request, 'wallpaper/next_page.json', {'images': images}, content_type='application/json; charset=UTF-8')
