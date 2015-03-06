# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.contrib.auth.models import User

from rest_framework import routers

from users.api.views import BaseProfileViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'baseprofiles', BaseProfileViewSet)
router.register(r'users', UserViewSet)

appurls = patterns('',
    url(r'users/', include('users.urls', namespace='users')),
)

urlpatterns = patterns('',
    url(r'^m/', include(appurls, namespace='app')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT}),
)



