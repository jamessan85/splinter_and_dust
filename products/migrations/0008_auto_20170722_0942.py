# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-22 08:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20170722_0901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='company_banner',
        ),
        migrations.RemoveField(
            model_name='product',
            name='company_name',
        ),
    ]
