# -*- coding: utf-8 -*-

from django.contrib import admin

from .models import Image
from .models import Tag

# Register your models here.

admin.site.register(Tag)
admin.site.register(Image)
