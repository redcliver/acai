# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-04-07 20:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0008_auto_20190323_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemacai',
            name='acompanhamento',
            field=models.CharField(choices=[('N', 'Nada'), ('M', 'Mel'), ('L', 'Leite Condensado')], default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='itemmix',
            name='acompanhamento',
            field=models.CharField(choices=[('N', 'Nada'), ('M', 'Mel'), ('L', 'Leite Condensado')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='itemcasadinho',
            name='acompanhamento',
            field=models.CharField(choices=[('N', 'Nada'), ('M', 'Mel'), ('L', 'Leite Condensado')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='itemcreme',
            name='acompanhamento',
            field=models.CharField(choices=[('N', 'Nada'), ('M', 'Mel'), ('L', 'Leite Condensado')], default='N', max_length=1),
        ),
    ]
