# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
# Create your models here.


@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(verbose_name=_('Name'), max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')


@python_2_unicode_compatible
class Image(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=25, db_index=True)
    url = models.URLField(verbose_name=_('URL'), unique=True)
    tags = models.ManyToManyField(Tag, verbose_name=_('Tags'))
    publishedAt = models.DateField(verbose_name=_('Published Date'),
                                   auto_now_add=True)
    uuid = models.CharField(verbose_name=_('UUID'), max_length=32, unique=True)
    show = models.BooleanField(verbose_name=_('Show'),
                               help_text=_('Whether to show this image'),
                               default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Image')
        verbose_name_plural = _('Images')
