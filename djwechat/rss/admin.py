# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Article
from .models import Author
from .models import Category
from .models import FeedChannel
# Register your models here.

admin.site.register(FeedChannel)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Article)
