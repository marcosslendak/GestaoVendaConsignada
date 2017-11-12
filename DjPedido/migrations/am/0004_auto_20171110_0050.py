# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-10 00:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DjPedido', '0003_auto_20171106_2359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Devolucao',
            fields=[
                ('pedido_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='DjPedido.Pedido')),
            ],
            bases=('DjPedido.pedido',),
        ),
        migrations.CreateModel(
            name='ItensDevolucao',
            fields=[
                ('itenspedido_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='DjPedido.ItensPedido')),
            ],
            bases=('DjPedido.itenspedido',),
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='informacoes',
        ),
        migrations.AddField(
            model_name='itenspedido',
            name='qtdDevolvida',
            field=models.IntegerField(blank=True, null=True, verbose_name='Quantidade devolvida'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='ativo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='pedido',
            name='dtFechamento',
            field=models.DateField(blank=True, null=True, verbose_name='Data do fechamento'),
        ),
    ]