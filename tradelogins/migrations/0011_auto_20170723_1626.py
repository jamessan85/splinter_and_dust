# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-23 15:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tradelogins', '0010_accountinfo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountinfo',
            name='user',
        ),
        migrations.AlterField(
            model_name='accountinfo',
            name='account_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
