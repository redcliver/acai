# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 14:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0004_auto_20170829_0004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemmshake',
            old_name='sorvete_item',
            new_name='mshake_item',
        ),
    ]
