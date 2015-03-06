# -*- coding: utf-8 -*- 

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.contrib.auth.models import (
    User
)

class BaseProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(_("avatar"), blank=True)

    def __unicode__(self):
        return self.user.username
