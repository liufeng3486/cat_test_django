# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-21 03:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0007_auto_20160621_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request_data',
            name='value',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
