# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-05 22:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caixa', '0014_auto_20190305_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caixa',
            name='data',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 5, 19, 33, 36, 9869)),
        ),
    ]
