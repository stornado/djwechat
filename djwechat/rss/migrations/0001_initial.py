# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-03 06:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('link', models.URLField(verbose_name='Link')),
                ('content', models.TextField(verbose_name='Content')),
                ('publishedAt', models.DateTimeField(verbose_name='Published Time')),
                ('updatedAt', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('show', models.BooleanField(default=True, help_text='Whether to show', verbose_name='Show')),
            ],
            options={
                'ordering': ('-updatedAt', '-publishedAt'),
                'verbose_name_plural': 'Articles',
                'verbose_name': 'Article',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Name')),
                ('link', models.URLField(blank=True, null=True, verbose_name='Homepage')),
            ],
            options={
                'verbose_name_plural': 'Authors',
                'verbose_name': 'Author',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=25, unique=True, verbose_name='Tag')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'verbose_name': 'Category',
            },
        ),
        migrations.CreateModel(
            name='FeedChannel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('link', models.URLField(verbose_name='Feed Link')),
                ('website', models.URLField(verbose_name='Official Website')),
                ('subtitle', models.TextField(blank=True, null=True, verbose_name='Subtitle')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
            options={
                'ordering': ('title',),
                'verbose_name_plural': 'Feed Channels',
                'verbose_name': 'Feed Channel',
            },
        ),
        migrations.AlterUniqueTogether(
            name='feedchannel',
            unique_together=set([('title', 'link')]),
        ),
        migrations.AlterUniqueTogether(
            name='author',
            unique_together=set([('name', 'link')]),
        ),
        migrations.AddField(
            model_name='article',
            name='authors',
            field=models.ManyToManyField(to='rss.Author', verbose_name='Authors'),
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(to='rss.Category', verbose_name='Categories'),
        ),
        migrations.AddField(
            model_name='article',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rss.FeedChannel', verbose_name='FeedChannel'),
        ),
        migrations.AlterUniqueTogether(
            name='article',
            unique_together=set([('channel', 'title', 'link')]),
        ),
    ]