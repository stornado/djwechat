# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class WallpaperConfig(AppConfig):
    name = 'wallpaper'
    verbose_name = _('Wallpaper')
