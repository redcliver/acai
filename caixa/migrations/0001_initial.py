# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 20:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='caixa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(default='Entrada', max_length=20)),
                ('item', models.CharField(blank=True, max_length=200, null=True)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('data', models.DateTimeField(default=datetime.datetime(2017, 8, 22, 20, 56, 17, 648604))),
                ('total', models.DecimalField(decimal_places=2, max_digits=12)),
            ],
        ),
    ]
