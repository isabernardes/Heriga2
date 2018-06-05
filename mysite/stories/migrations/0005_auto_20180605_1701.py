# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-05 17:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0004_auto_20180605_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
