# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 21:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='acai',
            old_name='obs',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='casadinho',
            old_name='obs',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='creme',
            old_name='obs',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='fondue',
            old_name='obs',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='mix',
            old_name='obs',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='mshake',
            old_name='obs',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='petit',
            old_name='obs',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='obs',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='sorvete',
            old_name='obs',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='suco',
            old_name='obs',
            new_name='img',
        ),
    ]
