# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from django.shortcuts import render
from serializers import IdentitySerializer

# Create your views here.
from server.models import Identity


class IdentityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Identity.objects.all()
    serializer_class = IdentitySerializer
