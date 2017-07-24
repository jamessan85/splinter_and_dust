# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.

RANGE_CHOICES = [
    ('Frames', 'Frames'),
    ('Artwork', 'Artwork'),
    ('Furniture', 'Furniture'),
    ('Upcycled', 'Upcycled'),
]

class Product(models.Model):
    title = models.CharField(max_length=50, null=True)
    content = models.TextField(max_length=200, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null = True)
    image = models.ImageField(upload_to="images", blank=False, null=True)
    product_info = models.TextField (max_length=200, null=True)
    creator = models.TextField (max_length=200, null=True)
    userid = models.IntegerField(null=True)
    range = models.CharField(max_length=15, choices=RANGE_CHOICES, null=True)



    def __unicode__(self):
        return self.title

class Collection(models.Model):
    range = models.CharField(max_length=15, choices=RANGE_CHOICES, null=True)

    def __unicode__(self):
        return self.range