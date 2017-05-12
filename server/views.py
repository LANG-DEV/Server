# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from django.http import *
from serializers import IdentitySerializer
import json
import jwt

# Create your views here.
from server.models import Identity

PRIVATE_KEY = 'secret'

class IdentityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Identity.objects.all()
    serializer_class = IdentitySerializer

    @list_route(methods=['post']) # /signup
    def signup(self, request, pk=None):
        print '/identity/signup', request.POST
        if not request.POST.get('user_info'):
            return HttpResponseBadRequest()
        try:
            user_info = json.loads(request.POST.get('user_info'))
        except ValueError:
            return HttpResponseBadRequest()
        print 'creating'
        res = Identity.create(user_info)
        print res
        if res:
            return Response(True)
        else:
            return HttpResponseForbidden()

    @list_route(methods=['post'])
    def login(self, request, pk=None):
        print '/identity/login', request.POST
        if not request.POST.get('username') or not request.POST.get('password'):
            return HttpResponseBadRequest()
        print 'try login'
        res = Identity.login(request.POST.get('username'), request.POST.get('password'))
        if res:
            # include the generated jwt in response
            # TODO: jwt payload??
            token = jwt.encode({
                'username': request.POST.get('username')
                # 'exp': 100000 expiration time
            }, PRIVATE_KEY)
            response = json.dumps({'jwt': token, 'success': res})
            return Response(response)
        else:
            return HttpResponseForbidden()
