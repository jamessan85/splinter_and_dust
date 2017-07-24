# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils import timezone
from django.conf import settings

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
    user_type = models.CharField(max_length=2, choices=type_choices, default='C')
    objects = AccountUserManager()

class AccountInfo(models.Model):

    company_name = models.CharField (max_length=25, null=True)
    company_banner = models.ImageField(upload_to="images/banners", blank=False, null=True)
    account = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user', null=True)

    def __unicode__(self):
        return self.company_name