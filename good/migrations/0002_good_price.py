# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-14 06:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('good', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='price',
            field=models.FloatField(default=0, verbose_name='\u5355\u4ef7'),
        ),
    ]
