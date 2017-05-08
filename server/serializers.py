from rest_framework import serializers

from server.models import Identity, LangGroup, Message, ChatRoom, Location, Board


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


class BoardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Board
        fields = ('url', 'group_id', 'location_id', 'time', 'time_created', 'time_last_modified')


class ChatRoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ('url', 'event_id', 'user_count', 'time_created', 'time_last_modified')


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = ('url', 'latitude', 'longitude', 'address', 'zip')