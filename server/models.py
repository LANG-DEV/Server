# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

import django
from django.db import models
from django.utils import timezone


# Create your models here.

class Identity(models.Model):
    USER_STATUS = (
        'ACTIVE',
        'OFFLINE',
        'NEW',
    )
    #user_id = models.CharField(max_length=36, primary_key=True)
    username = models.CharField(max_length=20, unique=True, db_index=True)
    #icon = models.ForeignKey('Image.image_id', on_delete=models.SET_NULL)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=36)
    last_name = models.CharField(max_length=36)
    status = models.CharField(max_length=10, default='NEW')#choices=USER_STATUS, default='NEW')
    #email = models.CharField(max_length=50)
    #birthday = models.DateField()
    #facebook = models.CharField(max_length=50)
    #deviceToken = models.CharField(max_length=152)
    #platform = models.CharField(max_length=10, choices=('android', 'ios'))
    #timeCreated = models.DateField(default=timezone.now)
    #timeLastModified = models.DateField(default=timezone.now)

    def passwordValidate(self, password):
        # check length
        if len(password) < 8 or len(password) > 20:
            return False

        # check contains lowercase
        lowerCase = False
        for i in range('a', 'z' + 1):
            if i in password:
                lowerCase = True
                break
        if not lowerCase:
            return False

        # check contains uppercase
        upperCase = False
        for i in range('A', 'Z' + 1):
            if i in password:
                upperCase = True
                break
        if not upperCase:
            return False

        num = False
        for i in range('0', '9'):
            if i in password:
                num = True
                break
        if not num:
            return False

    @classmethod
    def create(cls, user_info):
        if not cls.passwordValidate(user_info['password']):
            return False
        identity = cls(
            user_id=uuid.uuid4(),
            username=user_info['username'],
            password=user_info['password'],
            first_name=user_info['first_name'],
            last_name=user_info['last_name'],
            email=user_info['email'],)

class LangGroup(models.Model):
    # group_id = models.CharField(max_length=36, primary_key=True)
    chat_room_id = models.ForeignKey('ChatRoom', to_field='id', on_delete=models.CASCADE)
    board_id = models.ForeignKey('Board', to_field='id', on_delete=models.CASCADE)
    capacity = models.IntegerField()
    user_count = models.IntegerField()
    name = models.CharField(max_length=100)
    invitation_code = models.CharField(max_length=6)
    time_created = models.DateField(default=timezone.now)
    time_last_modified = models.DateField(default=timezone.now)

class Message(models.Model):
    MESSAGE_TYPE = (
        ('pm', 'PLAIN_MESSAGE'),
        ('pl', 'POLL'),
        ('mr', 'MERGE_REQUEST'),
        ('gm', 'INTER_GROUP_MESSAGE'),
        ('nm', 'NEW_MEMBER'),
    )
    # message_id = models.CharField(max_lengoth=36, primary_key=True)
    chat_room_id = models.ForeignKey('ChatRoom', to_field='id', on_delete=models.CASCADE)
    message_content = models.CharField(max_length=1000)
    message_type = models.CharField(max_length=20, choices=MESSAGE_TYPE)
    time_created = models.DateField(default=django.utils.timezone.now)
    time_last_modified = models.DateField(default=django.utils.timezone.now)

class Board(models.Model):
    group_id = models.ForeignKey('LangGroup', to_field='id', on_delete=models.CASCADE)
    location_id = models.ForeignKey('Location', to_field='id', on_delete=models.CASCADE)
    time = models.DateTimeField()
    time_created = models.TimeField(default=django.utils.timezone.now)
    time_last_modified = models.TimeField(default=django.utils.timezone.now)

class ChatRoom(models.Model):
    event_id = models.ForeignKey(LangGroup, to_field='id', on_delete=models.CASCADE)
    user_count = models.IntegerField()
    time_created = models.DateField(default=django.utils.timezone.now)
    time_last_modified = models.DateField(default=django.utils.timezone.now)

class Location(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longtitude = models.DecimalField(max_digits=9, decimal_places=6)
    address = models.CharField(max_length=100)
    zip = models.IntegerField()
