# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

# Create your models here.


@python_2_unicode_compatible
class FeedChannel(models.Model):
    title = models.CharField(verbose_name=_('Title'),
                             max_length=50)
    link = models.URLField(verbose_name=_('Feed Link'))
    website = models.URLField(verbose_name=_('Official Website'))
    subtitle = models.TextField(verbose_name=_('Subtitle'),
                                null=True, blank=True)
    description = models.TextField(verbose_name=_('Description'),
                                   null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Feed Channel')
        verbose_name_plural = _('Feed Channels')
        unique_together = (('title', 'link'),)
        ordering = ('title',)


@python_2_unicode_compatible
class Author(models.Model):
    name = models.CharField(verbose_name=_('Name'),
                            max_length=25)
    link = models.URLField(verbose_name=_('Homepage'),
                           null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')
        unique_together = (('name', 'link'),)


@python_2_unicode_compatible
class Category(models.Model):
    tag = models.CharField(verbose_name=_('Tag'),
                           max_length=25,
                           unique=True)

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


@python_2_unicode_compatible
class Article(models.Model):
    channel = models.ForeignKey(to=FeedChannel,
                                verbose_name=_('Feed Channel'))
    title = models.CharField(verbose_name=_('Title'),
                             max_length=255)
    link = models.URLField(verbose_name=_('Link'))
    authors = models.ManyToManyField(Author,
                                     verbose_name=_('Authors'))
    categories = models.ManyToManyField(Category,
                                        verbose_name=_('Categories'))
    content = models.TextField(verbose_name=_('Content'))
    publishedAt = models.DateTimeField(verbose_name=_('Published Time'))
    updatedAt = models.DateTimeField(verbose_name=_('Updated Time'),
                                     auto_now=True)
    show = models.BooleanField(verbose_name=_('Show'),
                               help_text=_('Whether to show this article'),
                               default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Article')
        verbose_name_plural = _('Articles')
        unique_together = (('channel', 'title', 'link'),)
        ordering = ('-updatedAt', '-publishedAt')
