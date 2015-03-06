# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from rest_framework import viewsets
from users.api.serializers import BaseProfileSerializer, UserSerializer
from users.models import BaseProfile


class BaseProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = BaseProfile.objects.all()
    serializer_class = BaseProfileSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
