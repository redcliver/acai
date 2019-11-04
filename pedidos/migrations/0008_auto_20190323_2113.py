# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-24 00:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0007_comanda_cli'),
    ]

    operations = [
        migrations.AddField(
            model_name='comanda',
            name='tipo',
            field=models.CharField(choices=[('1', 'Local'), ('2', 'Viagem'), ('3', 'Entrega')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='comanda',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]