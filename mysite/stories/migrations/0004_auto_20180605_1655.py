# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-05 16:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_story'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='story',
            unique_together=set([('slug', 'community')]),
        ),
    ]
