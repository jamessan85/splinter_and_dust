# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-25 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradelogins', '0013_user_stripe_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountinfo',
            name='formstatus',
            field=models.CharField(default='D', max_length=2, null=True),
        ),
    ]
