# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-17 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_comments_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]