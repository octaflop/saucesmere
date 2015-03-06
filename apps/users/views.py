# -*- coding: utf-8 -*-

from django.shortcuts import render

def index(request):
    ctx = {}
    template_name = 'users/index.html'

    return render(request, template_name, ctx)
