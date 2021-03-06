# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-21 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradelogins', '0002_user_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address_line_1',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='address_line_2',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='company_logo',
            field=models.ImageField(null=True, upload_to='images/banners'),
        ),
        migrations.AddField(
            model_name='user',
            name='company_name',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='county',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
