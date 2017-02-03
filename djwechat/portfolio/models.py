# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import gettext_lazy as _

from uuid import uuid4

# Create your models here.


@python_2_unicode_compatible
class Banner(models.Model):
    ''' Banner '''
    title = models.CharField(verbose_name=_('Title'),
                             max_length=15)
    link = models.URLField(verbose_name=_('Link'))
    image = models.URLField(verbose_name=_('ImageURL'))
    description = models.TextField(verbose_name=_('Description'),
                                   null=True, blank=True)
    uuid = models.UUIDField(verbose_name=_('UUID'), default=uuid4)
    order = models.SmallIntegerField(verbose_name=_('Order'),
                                     default=0,
                                     help_text=_('The order of the banner'))

    title_size = models.FloatField(verbose_name=_('Title Size'),
                                   default=1.5,
                                   help_text=_('Title size use rem'))
    title_color = models.CharField(verbose_name=_('Title Color'),
                                   default='#ffffff',
                                   max_length=15)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'portfolio_banner'
        verbose_name = _('Banner')
        verbose_name_plural = _('Banners')


@python_2_unicode_compatible
class User(models.Model):
    ''' 个人主页 '''
    name = models.CharField(verbose_name=_('Name'),
                            max_length=25)
    email = models.EmailField(verbose_name=_('Email'),
                              null=True, blank=True)
    phone = models.CharField(verbose_name=_('Phone'),
                             max_length=15,
                             null=True, blank=True)
    nickname = models.CharField(verbose_name=_('Nick Name'),
                                max_length=25,
                                null=True, blank=True)
    description = models.TextField(verbose_name=_('Description'),
                                   null=True, blank=True)  # 备注

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'portfolio_user'
        verbose_name = _('User')
        verbose_name_plural = _('Users')


@python_2_unicode_compatible
class SNS(models.Model):
    ''' 三方登录方式 '''
    user = models.ForeignKey(verbose_name=_('User'), to=User)
    name = models.CharField(verbose_name=_('Name'), max_length=15)  # 名字
    sns_id = models.CharField(verbose_name=_('ID'), max_length=15)  # 三方登录方式ID
    avatar = models.URLField(verbose_name=_('AvatarURL'))  # 头像
    link = models.URLField(verbose_name=_('Link'),  # 三方登录方式主页链接
                           help_text=_("The homepage of the platform"),
                           null=True, blank=True)
    icon = models.URLField(verbose_name=_('IconURL'),  # 三方平台图标
                           help_text=_("The SNS paltform's icon url"))
    platform = models.CharField(verbose_name=_('Platform'),  # 三方平台名称
                                max_length=15,
                                help_text=_("The SNS platform's name"))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'portfolio_sns'
        verbose_name = _('SNS')
        verbose_name_plural = _('SNS')


@python_2_unicode_compatible
class Skill(models.Model):
    ''' 技能，用于绘制技能评估表（技能雷达radar）'''
    user = models.ForeignKey(verbose_name=_('User'), to=User)
    name = models.CharField(verbose_name=_('Name'), max_length=15)  # 技能名
    level = models.PositiveSmallIntegerField(
        verbose_name=_('Level(0-100)'))  # 等级
    period = models.SmallIntegerField(verbose_name=_('Period(months)'))  # 使用时长
    description = models.TextField(verbose_name=_('Description'))  # 具体描述

    def __str__(self):
        return '%s(%d)' % (self.name, self.level)

    class Meta:
        db_table = 'portfolio_skill'
        verbose_name = _('Skill')
        verbose_name_plural = _('Skills')


@python_2_unicode_compatible
class Experience(models.Model):
    ''' 时间节点，用于绘制时间轴timeline '''
    user = models.ForeignKey(verbose_name=_('User'), to=User)
    start = models.DateField(verbose_name=_('Start'))  # 经历开始时间
    end = models.DateField(verbose_name=_('End'))  # 结束时间
    title = models.CharField(verbose_name=_('Title'), max_length=15)  # 标题
    description = models.TextField(verbose_name=_('Description'))  # 具体内容

    def __str__(self):
        return title

    class Meta:
        db_table = 'portfolio_milestone'
        verbose_name = _('Experience')
        verbose_name_plural = _('Experience')


@python_2_unicode_compatible
class Works(models.Model):
    ''' 作品，用于在作品集portfolio中展示 '''
    user = models.ForeignKey(verbose_name=_('User'), to=User)
    name = models.CharField(verbose_name=_('Name'), max_length=15)  # 作品名
    # sceenshots = models.
    url = models.URLField(verbose_name=_('URL'),
                          help_text=_('The works page'))
    description = models.TextField(verbose_name=_('Description'))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'portfolio_works'
        verbose_name = _('Works')
        verbose_name_plural = _('Works')


@python_2_unicode_compatible
class Expection(models.Model):
    ''' 期望，用于在期望 '''
    user = models.ForeignKey(verbose_name=_('User'), to=User)
    title = models.CharField(verbose_name=_('Title'), max_length=15)
    description = models.TextField(verbose_name=_('Description'))

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'portfolio_expection'
        verbose_name = _('Expection')
        verbose_name_plural = _('Expection')
