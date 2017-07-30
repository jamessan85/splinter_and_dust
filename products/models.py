# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
from django.db import models
from tinymce.models import HTMLField
from django.conf import settings

# Create your models here.

RANGE_CHOICES = [
    ('frames', 'Frames'),
    ('artwork', 'Artwork'),
    ('furniture', 'Furniture'),
    ('upcycled', 'Upcycled'),
]

class Product(models.Model):
    title = models.CharField(max_length=50, null=True)
    content = models.TextField(max_length=200, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null = True)
    image = models.ImageField(upload_to="images", blank=False, null=True)
    product_info = models.TextField (max_length=200, null=True)
    creator = HTMLField(blank=True, null=True)
    userid = models.IntegerField(null=True)
    range = models.CharField(max_length=15, choices=RANGE_CHOICES, null=True)

    # @property
    # def paypal_form(self):
    #     paypal_dict = {
    #         "business": settings.PAYPAL_RECEIVER_EMAIL,
    #         "amount": self.price,
    #         "currency": "GBP",
    #         "item_name": self.title,
    #         "invoice": "%s-%s" % (self.pk, uuid.uuid4()),
    #         "notify_url": settings.PAYPAL_NOTIFY_URL,
    #         "return_url": "%s/paypal-return" % settings.SITE_URL,
    #         "cancel_return": "%s/paypal-cancel" % settings.SITE_URL
    #     }
    #
    #     return PayPalPaymentsForm(initial=paypal_dict)

    def __unicode__(self):
        return self.title

class Collection(models.Model):
    range = models.CharField(max_length=15, choices=RANGE_CHOICES, null=True)

    def __unicode__(self):
        return self.range

