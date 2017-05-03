from django.contrib.auth.models import User, Group
from rest_framework import serializers

from server.models import Identity, LangGroup, Message


class IdentitySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Identity
        fields = ('url', 'username', 'password', 'first_name', 'last_name', 'status')

class LangGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LangGroup
        fields = ('url', 'chat_room_id', 'board_id', 'capacity', 'user_count', 'name', 'invitation_code', 'time_created', 'time_last_modified')

class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = ('url', 'chat_room_id', 'message_content', 'message_type', 'time_created', 'time_last_modified')