# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-13 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0002_auto_20160913_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='jewel',
            name='fineness',
            field=models.IntegerField(default=0),
        ),
    ]
