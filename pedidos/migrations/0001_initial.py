# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 20:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='acai',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('tamanho', models.CharField(choices=[('P', 'Pequeno'), ('G', 'Grande')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='adicional',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='casadinho',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('tamanho', models.CharField(choices=[('P', 'Pequeno'), ('G', 'Grande')], max_length=1)),
                ('adicionais', models.ManyToManyField(to='pedidos.adicional')),
            ],
        ),
        migrations.CreateModel(
            name='comanda',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('total', models.DecimalField(decimal_places=2, default='0', max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='creme',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('tamanho', models.CharField(choices=[('P', 'Pequeno'), ('G', 'Grande')], max_length=1)),
                ('adicionais', models.ManyToManyField(to='pedidos.adicional')),
            ],
        ),
        migrations.CreateModel(
            name='fondue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('adicionais', models.ManyToManyField(to='pedidos.adicional')),
            ],
        ),
        migrations.CreateModel(
            name='itemacai',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('qnt', models.IntegerField(default=1)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('acai_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.acai')),
                ('adicionais', models.ManyToManyField(to='pedidos.adicional')),
            ],
        ),
        migrations.CreateModel(
            name='itemcasadinho',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('acompanhamento', models.CharField(choices=[('M', 'Mel'), ('L', 'Leite Condensado')], max_length=1)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('qnt', models.IntegerField(default=1)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('adicionais', models.ManyToManyField(to='pedidos.adicional')),
                ('casadinho_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.casadinho')),
            ],
        ),
        migrations.CreateModel(
            name='itemcreme',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('acompanhamento', models.CharField(choices=[('M', 'Mel'), ('L', 'Leite Condensado')], max_length=1)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('qnt', models.IntegerField(default=1)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('adicionais', models.ManyToManyField(to='pedidos.adicional')),
                ('casadinho_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.creme')),
            ],
        ),
        migrations.CreateModel(
            name='itemfondue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('qnt', models.IntegerField(default=1)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('adicionais', models.ManyToManyField(to='pedidos.adicional')),
                ('fondue_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.fondue')),
            ],
        ),
        migrations.CreateModel(
            name='itemmix',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('qnt', models.IntegerField(default=1)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('adicionais', models.ManyToManyField(to='pedidos.adicional')),
            ],
        ),
        migrations.CreateModel(
            name='itemmshake',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('qnt', models.IntegerField(default=1)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('adicionais', models.ManyToManyField(to='pedidos.adicional')),
            ],
        ),
        migrations.CreateModel(
            name='itempetit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('qnt', models.IntegerField(default=1)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('adicionais', models.ManyToManyField(to='pedidos.adicional')),
            ],
        ),
        migrations.CreateModel(
            name='itemproduto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('qnt', models.IntegerField(default=1)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='itemsorvete',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('qnt', models.IntegerField(default=1)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
                ('adicionais', models.ManyToManyField(to='pedidos.adicional')),
            ],
        ),
        migrations.CreateModel(
            name='itemsuco',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('add1', models.CharField(blank=True, choices=[('L', 'Leite'), ('S', 'Sorvete')], max_length=1, null=True)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('qnt', models.IntegerField(default=1)),
                ('total', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='mix',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('tamanho', models.CharField(choices=[('P', 'Pequeno'), ('G', 'Grande')], max_length=1)),
                ('adicionais', models.ManyToManyField(to='pedidos.adicional')),
            ],
        ),
        migrations.CreateModel(
            name='mshake',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('tamanho', models.CharField(choices=[('P', 'Pequeno'), ('G', 'Grande')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='petit',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
                ('adicionais', models.ManyToManyField(to='pedidos.adicional')),
            ],
        ),
        migrations.CreateModel(
            name='produto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='sorvete',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='suco',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=200)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('obs', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='itemsuco',
            name='suco_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.suco'),
        ),
        migrations.AddField(
            model_name='itemsorvete',
            name='sorvete_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.sorvete'),
        ),
        migrations.AddField(
            model_name='itemproduto',
            name='produto_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.produto'),
        ),
        migrations.AddField(
            model_name='itempetit',
            name='petit_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.petit'),
        ),
        migrations.AddField(
            model_name='itemmshake',
            name='sorvete_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.mshake'),
        ),
        migrations.AddField(
            model_name='itemmix',
            name='mix_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.mix'),
        ),
        migrations.AddField(
            model_name='comanda',
            name='acais',
            field=models.ManyToManyField(to='pedidos.itemacai'),
        ),
        migrations.AddField(
            model_name='comanda',
            name='casadinhos',
            field=models.ManyToManyField(to='pedidos.itemcasadinho'),
        ),
        migrations.AddField(
            model_name='comanda',
            name='cremes',
            field=models.ManyToManyField(to='pedidos.itemcreme'),
        ),
        migrations.AddField(
            model_name='comanda',
            name='fondues',
            field=models.ManyToManyField(to='pedidos.itemfondue'),
        ),
        migrations.AddField(
            model_name='comanda',
            name='mixs',
            field=models.ManyToManyField(to='pedidos.itemmix'),
        ),
        migrations.AddField(
            model_name='comanda',
            name='mshakes',
            field=models.ManyToManyField(to='pedidos.itemmshake'),
        ),
        migrations.AddField(
            model_name='comanda',
            name='petits',
            field=models.ManyToManyField(to='pedidos.itempetit'),
        ),
        migrations.AddField(
            model_name='comanda',
            name='produtos',
            field=models.ManyToManyField(to='pedidos.itemproduto'),
        ),
        migrations.AddField(
            model_name='comanda',
            name='sorvetes',
            field=models.ManyToManyField(to='pedidos.itemsorvete'),
        ),
        migrations.AddField(
            model_name='comanda',
            name='sucos',
            field=models.ManyToManyField(to='pedidos.itemsuco'),
        ),
        migrations.AddField(
            model_name='acai',
            name='adicionais',
            field=models.ManyToManyField(to='pedidos.adicional'),
        ),
    ]
