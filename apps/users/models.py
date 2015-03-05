# -*- coding: utf-8 -*- 

from django.conf import settings
from django.db import models
from django.contrib.auth import User
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

class SauceUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the
        . given email,
        favorite topping, and password.
        """
        if not email:
            msg = "Users must have an email address"
            raise ValueError(msg)
        user = self.model(
            email=TwoScoopsUserManager.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        creates a superuser with the given email & password
        """
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class SauceUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name=_("Email Address"), 
        max_length=255, 
        unique=True,
        db_index=True)
    avatar = models.ImageField(_("avatar"), blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["",]

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = SauceUserManager()

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def __unicode__(self):
        return self.email
