# -*- coding: utf-8 -*-
from django.shortcuts import render
from models import Banner, Experience, Skill
# Create your views here.


def home(request):
    template = 'portfolio/index.html'
    context = {'banners': Banner.objects.all().order_by('order', 'id'),
               'experience': Experience.objects.all().order_by('start', 'id'),
               'skills': Skill.objects.all()}
    return render(request, template, context)


def banner(request, banner_id):
    pass
