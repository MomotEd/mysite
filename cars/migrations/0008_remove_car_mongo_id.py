# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-13 08:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_auto_20160413_0751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='mongo_id',
        ),
    ]
