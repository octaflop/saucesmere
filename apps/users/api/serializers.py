# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.conf import settings
from users.models import BaseProfile
from rest_framework import serializers

class BaseProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BaseProfile
        fields = ('url', 'avatar', 'user',)
        depth = 1

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

