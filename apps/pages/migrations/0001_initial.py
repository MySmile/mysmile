# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.pages.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('slug', models.SlugField(unique=True)),
                ('color', models.CharField(help_text='Click once with the mouse to select                                         a color, and then twice to save', max_length=500, default='#FDA132')),
                ('photo', apps.pages.models.ImageField(upload_to='images/', null=True, blank=True)),
                ('sortorder', models.IntegerField(unique=True, verbose_name='Sort order', default=apps.pages.models.create_default_sortorder)),
                ('status', models.IntegerField(choices=[(0, 'draft'), (1, 'published')], default=0)),
                ('ptype', models.IntegerField(choices=[(0, 'inner page'), (1, 'menu page'), (2, 'api page'), (3, 'api & menu page')], verbose_name='Page type', default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-ptype', 'sortorder', 'status'],
                'db_table': 'Page',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Page_translation',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('lang', models.CharField(choices=[('en', 'English'), ('uk', 'Українська'), ('ru', 'Русский')], max_length=500, default='en')),
                ('menu', models.CharField(max_length=500)),
                ('name', models.CharField(null=True, max_length=500, blank=True)),
                ('col_central', models.TextField()),
                ('youtube', models.CharField(help_text='Link to youtube video.                                Max length url =  2048 characters', null=True, max_length=500, blank=True)),
                ('col_right', models.TextField(null=True, blank=True)),
                ('col_bottom_1', models.TextField(null=True, blank=True)),
                ('col_bottom_2', models.TextField(null=True, blank=True)),
                ('col_bottom_3', models.TextField(null=True, blank=True)),
                ('meta_title', models.CharField(max_length=500)),
                ('meta_description', models.CharField(max_length=500)),
                ('meta_keywords', models.CharField(max_length=500)),
                ('photo_alt', models.CharField(null=True, max_length=500, blank=True)),
                ('photo_description', models.CharField(null=True, max_length=500, blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('page', models.ForeignKey(to='pages.Page')),
            ],
            options={
                'ordering': ['lang'],
                'verbose_name': 'Translation',
                'db_table': 'Page_translation',
                'verbose_name_plural': 'Translations',
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='page_translation',
            unique_together=set([('page', 'lang')]),
        ),
    ]
