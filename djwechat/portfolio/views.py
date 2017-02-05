# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from models import Banner
from models import Experience
from models import Skill
from models import User
# Create your views here.


def home(request, uid=1):
    user = get_object_or_404(User, pk=uid)
    template = 'portfolio/index.html'
    context = {'banners': Banner.objects.all().order_by('order', 'id'),
               'experience': Experience.objects.filter(user=user).order_by('start', 'id'),
               'skills': Skill.objects.filter(user=user)}
    return render(request, template, context)


def banner(request, banner_id):
    pass
