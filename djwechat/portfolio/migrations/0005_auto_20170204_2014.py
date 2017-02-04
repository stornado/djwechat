# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20170204_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='banner',
            name='title_color',
        ),
        migrations.RemoveField(
            model_name='banner',
            name='title_size',
        ),
        migrations.RemoveField(
            model_name='banner',
            name='uuid',
        ),
        migrations.AlterField(
            model_name='banner',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='sns',
            name='avatar',
            field=models.URLField(blank=True, null=True, verbose_name='AvatarURL'),
        ),
    ]