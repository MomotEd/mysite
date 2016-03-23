# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-23 08:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0003_catalog'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='file',
            field=models.FileField(default=django.utils.timezone.now, upload_to=b''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='catalog',
            name='upload_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 23, 8, 6, 44, 329111, tzinfo=utc)),
            preserve_default=False,
        ),
    ]