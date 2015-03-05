# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Preferences',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('key', models.CharField(unique=True, max_length=500)),
                ('value', models.CharField(null=True, max_length=500, blank=True)),
                ('name', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Preference',
                'db_table': 'Preferences',
                'verbose_name_plural': 'Preferences',
            },
            bases=(models.Model,),
        ),
    ]
