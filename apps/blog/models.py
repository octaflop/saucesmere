# -*- coding: utf-8 -*-

import datetime, arrow

from django.db import models
from django.contrib.auth.models import User

from saucesmere.models.mixins import TimestampMixin

class Entry(TimestampMixin):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User)
    
    published_on = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)

    def __unicode__(self):
        return u"{self.title} by {self.author.first_name}".format(self=self)
