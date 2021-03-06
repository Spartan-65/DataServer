# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 15:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0003_auto_20171213_2302'),
        ('good', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_code', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='\u8ba2\u5355\u53f7')),
                ('goodname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='good.Good')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.User')),
            ],
        ),
    ]
