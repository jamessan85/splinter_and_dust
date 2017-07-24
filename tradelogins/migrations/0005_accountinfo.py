# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-21 19:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tradelogins', '0004_auto_20170721_2015'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.TextField(max_length=200, null=True)),
                ('company_banner', models.ImageField(null=True, upload_to='images/banners')),
            ],
        ),
    ]
