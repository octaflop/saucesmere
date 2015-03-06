# -*- coding: utf-8 -*-

from django.conf import settings
from users.models import BaseProfile
from rest_framework import serializers

class BaseProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BaseProfile
        fields = ('url', 'username', 'email', 'groups')

