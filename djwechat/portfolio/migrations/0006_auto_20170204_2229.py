# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20170204_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='image',
            field=models.URLField(blank=True, null=True, verbose_name='ImageURL'),
        ),
        migrations.AlterField(
            model_name='banner',
            name='title',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Title'),
        ),
    ]