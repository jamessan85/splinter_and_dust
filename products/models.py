# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
from django.db import models
from django.conf import settings

# Create your models here.

#for drop down menu in range
RANGE_CHOICES = [
    ('frames', 'Frames'),
    ('artwork', 'Artwork'),
    ('furniture', 'Furniture'),
    ('upcycled', 'Upcycled'),
]

#model for product info
class Product(models.Model):
    title = models.CharField(max_length=50, null=True)
    content = models.TextField(max_length=200, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null = True)
    image = models.ImageField(upload_to="images", blank=False, null=True)
    product_info = models.TextField (max_length=200, null=True)
    creator = models.CharField(max_length=50, blank=True, null=True)
    userid = models.IntegerField(null=True)
    range = models.CharField(max_length=15, choices=RANGE_CHOICES, null=True)

    def __unicode__(self):
        return self.title

#collection model for the navbar
class Collection(models.Model):
    range = models.CharField(max_length=15, choices=RANGE_CHOICES, null=True)

    def __unicode__(self):
        return self.range

