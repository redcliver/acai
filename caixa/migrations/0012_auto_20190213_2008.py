# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-02-13 23:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caixa', '0011_auto_20190213_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caixa',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2019, 2, 13, 20, 8, 24, 851587)),
        ),
    ]
