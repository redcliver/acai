# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-29 14:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caixa', '0007_auto_20180410_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caixa',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 29, 10, 59, 28, 943083)),
        ),
    ]
