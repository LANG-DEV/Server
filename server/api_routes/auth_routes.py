from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from django.http import HttpResponse


@api_view(['GET', 'POST'])
def login(request):
    data = {'token': 'abc'}
    return HttpResponse('Hello World')
    #return Response(data)


@api_view(['POST'])
def signup(request):
    pass