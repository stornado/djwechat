# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-05 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0007_auto_20170204_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='end',
            field=models.DateField(blank=True, null=True, verbose_name='End'),
        ),
    ]
