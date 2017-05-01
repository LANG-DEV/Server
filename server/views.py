# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
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

    @list_route(methods=['get', 'post'])
    def signup(self, request, pk=None):
        return Response({'Message': 'HelloWorld'})
