# -*- coding: utf-8 -*-

from django.contrib import admin
from users.models import BaseProfile

class BaseProfileAdmin(admin.ModelAdmin):
    class Meta:
        model = BaseProfile

admin.site.register(BaseProfile, BaseProfileAdmin)
