# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.


def home(request):
    template = 'portfolio/index.html'
    # template = 'portfolio/verticaltimeline.html'
    context = {}
    return render(request, template, context)


def banner(request, banner_id):
    pass
