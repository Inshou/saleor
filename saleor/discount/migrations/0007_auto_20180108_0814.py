# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-08 14:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django_prices.models


class Migration(migrations.Migration):

    dependencies = [
        ('discount', '0006_auto_20171129_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='categories',
            field=models.ManyToManyField(blank=True, to='product.Category'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='sale',
            name='products',
            field=models.ManyToManyField(blank=True, to='product.Product'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='type',
            field=models.CharField(choices=[('fixed', 'RUB'), ('percentage', '%')], default='fixed', max_length=10),
        ),
        migrations.AlterField(
            model_name='sale',
            name='value',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='apply_to',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Category'),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='code',
            field=models.CharField(db_index=True, max_length=12, unique=True),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='discount_value',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='discount_value_type',
            field=models.CharField(choices=[('fixed', 'RUB'), ('percentage', '%')], default='fixed', max_length=10),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='limit',
            field=django_prices.models.MoneyField(blank=True, currency='RUB', decimal_places=2, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Product'),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='start_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='type',
            field=models.CharField(choices=[('value', 'All purchases'), ('product', 'One product'), ('category', 'A category of products'), ('shipping', 'Shipping')], default='value', max_length=20),
        ),
        migrations.AlterField(
            model_name='voucher',
            name='usage_limit',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
