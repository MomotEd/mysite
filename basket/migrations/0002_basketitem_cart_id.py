# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-25 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basketitem',
            name='cart_id',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
