# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-29 21:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='community',
            options={'verbose_name': 'Community', 'verbose_name_plural': 'Communities'},
        ),
    ]
