# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-01 12:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mcs', '0013_auto_20160901_1207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='areas',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='areas',
            name='lon',
        ),
        migrations.RemoveField(
            model_name='food',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='food',
            name='lon',
        ),
        migrations.RemoveField(
            model_name='health',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='health',
            name='lon',
        ),
        migrations.RemoveField(
            model_name='shelter',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='shelter',
            name='lon',
        ),
        migrations.RemoveField(
            model_name='victims',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='victims',
            name='lon',
        ),
    ]
