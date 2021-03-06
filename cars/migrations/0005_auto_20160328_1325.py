# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-28 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_auto_20160323_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='acceleration',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='car',
            name='cylinders',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='car',
            name='displacement',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='car',
            name='horsepower',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='car',
            name='mpg',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='car',
            name='weight',
            field=models.CharField(max_length=30),
        ),
    ]
