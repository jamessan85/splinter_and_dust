# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-21 19:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradelogins', '0005_accountinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountinfo',
            name='account_id',
            field=models.IntegerField(null=True),
        ),
    ]
