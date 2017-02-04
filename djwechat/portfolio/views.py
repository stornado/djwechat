# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import Banner
# Create your views here.


def home(request):
    # template = 'portfolio/index.html'
    template = 'portfolio/base_site.html'
    # template = 'portfolio/verticaltimeline.html'
    context = {'banners': Banner.objects.all()}
    return render(request, template, context)


def banner(request, banner_id):
    pass
