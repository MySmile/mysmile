# -*- coding: utf-8 -*-
import os
from django.core.management import call_command
from django.db import models, migrations

from mysmile.settings.base import BASE_DIR


class Migration(migrations.Migration):

    def load_migration(apps, schema_editor):
            path_to_fixture = os.path.join(
                BASE_DIR, '../apps/preferences/fixtures/preferences.json')
            call_command('loaddata', path_to_fixture)

    dependencies = []

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
            migrations.RunPython(load_migration)
            ]
