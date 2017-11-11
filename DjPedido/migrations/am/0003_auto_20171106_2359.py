# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-06 23:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('DjPedido', '0002_auto_20171104_2159'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pedido',
            options={'verbose_name_plural': 'Pedidos'},
        ),
        migrations.RemoveField(
            model_name='itenspedido',
            name='qtdDevolvida',
        ),
        migrations.RemoveField(
            model_name='itenspedido',
            name='vlrDescontoUnitario',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='ativo',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='dtAbertura',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='dtFechamento',
        ),
        migrations.AddField(
            model_name='pedido',
            name='descricao',
            field=models.CharField(default=1, max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='dtPedido',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Data do pedido'),
            preserve_default=False,
        ),
    ]
