# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from django.shortcuts import render
from serializers import IdentitySerializer, LangGroupSerializer, MessageSerializer, BoardSerializer, ChatRoomSerializer, LocationSerializer

# Create your views here.
from server.models import Identity, LangGroup, Message, Board, ChatRoom, Location


class IdentityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Identity.objects.all()
    serializer_class = IdentitySerializer

    @list_route(methods=['get', 'post'])
    def signup(self, request, pk=None):
        return Response({'Message': 'HelloWorld'})


class LangGroupViewSet(viewsets.ModelViewSet):
    queryset = LangGroup.objects.all()
    serializer_class = LangGroupSerializer


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class ChatRoomViewSet(viewsets.ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer