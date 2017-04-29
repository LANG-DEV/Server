from django.contrib.auth.models import User, Group
from rest_framework import serializers

from server.models import Identity


class IdentitySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Identity
        fields = ('url', 'username', 'password', 'first_name', 'last_name', 'status')
