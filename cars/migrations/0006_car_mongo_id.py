# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-11 13:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_auto_20160328_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='mongo_id',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]
