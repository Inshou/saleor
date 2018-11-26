# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 10:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_prices.models
from django.contrib.postgres import fields


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_auto_20170113_0435'),
    ]

    replaces = [
        ('cart', '0002_auto_20170206_0407'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cart',
            options={'ordering': ('-last_status_change',), 'verbose_name': 'Cart', 'verbose_name_plural': 'Carts'},
        ),
        migrations.AlterModelOptions(
            name='cartline',
            options={'verbose_name': 'Cart line', 'verbose_name_plural': 'Cart lines'},
        ),
        migrations.AlterField(
            model_name='cart',
            name='checkout_data',
            field=fields.JSONField(editable=False, null=True, verbose_name='checkout data'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(default=0, verbose_name='quantity'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=django_prices.models.MoneyField(currency='RUB', decimal_places=2, default=0, max_digits=12, verbose_name='total'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='voucher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='discount.Voucher', verbose_name='token'),
        ),
        migrations.AlterField(
            model_name='cartline',
            name='cart',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='checkout.Cart', verbose_name='cart'),
        ),
        migrations.AlterField(
            model_name='cartline',
            name='data',
            field=fields.JSONField(blank=True, default=dict, verbose_name='data'),
        ),
    ]
