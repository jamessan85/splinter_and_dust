# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-26 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20170726_0734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='stripe_id',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]
