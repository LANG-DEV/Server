# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

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
