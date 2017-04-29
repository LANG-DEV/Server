# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from server.data_model import identity_model
from server.serializers import IdentitySerializer


class IdentityViewSet(viewsets.ModelViewSet):
    queryset = identity_model.IdentityModel.objects.all()
    serializer_class = IdentitySerializer
