# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-12 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_story'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='story',
            options={'verbose_name': 'Story', 'verbose_name_plural': 'Stories'},
        ),
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