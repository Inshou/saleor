# Generated by Django 2.1.3 on 2018-11-25 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0067_auto_20181102_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='language_code',
            field=models.CharField(default='ru', max_length=35),
        ),
    ]