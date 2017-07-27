# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils import timezone
from django.conf import settings
from products.models import Product

# Create your models here

class AccountUserManager(UserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):

        now = timezone.now()
        if not email:
            raise ValueError('The given username must be set')

        email = self.normalize_email(email)
        user = self.model(username=email, email=email,
                          is_staff=is_staff, is_active=True,
                        is_superuser=is_superuser, date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

class User(AbstractUser):

    type_choices = (
        ('T','Trade'),
        ('C', 'Customer'),
    )
    stripe_id = models.CharField(max_length=40, default='')
    user_type = models.CharField(max_length=2, choices=type_choices, default=' ')
    objects = AccountUserManager()

class AccountInfo(models.Model):

    company_name = models.CharField (max_length=25, null=True)
    company_banner = models.ImageField(upload_to="images/banners", blank=False, null=True)
    company_logo_square = models.ImageField(upload_to="images/logo_sqaure", blank=False, null=True)
    company_blurb = models.TextField (max_length=1000, null=True)
    account = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user', null=True)
    formstatus = models.CharField(max_length=2, default='D', null=True)

    def __unicode__(self):
        return self.company_name

class Purchase(models.Model):
    stripe_id = models.CharField(max_length=40, default='')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='product', null=True)
    product = models.ForeignKey(Product, related_name='product', null=True)
    title = models.CharField(max_length=50, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    product_info = models.TextField(max_length=200, null=True)

    def __unicode__(self):
        return self.product