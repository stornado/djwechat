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
    all_images = get_list_or_404(Image)
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
        return JsonResponse()


def search(request):
    return JsonResponse()
