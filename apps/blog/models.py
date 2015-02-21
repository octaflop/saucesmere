# -*- coding: utf-8 -*-

import datetime, arrow

from django.db import models

from saucesmere.models.mixins import TimestampMixin

class Entry(TimestampMixin):
    pass
