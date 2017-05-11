# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

from django.db import models
from django.core.exceptions import ObjectDoesNotExist


# Create your models here.

class Identity(models.Model):
    USER_STATUS = (
        'ACTIVE',
        'OFFLINE',
        'NEW',
    )
    # user_id = models.CharField(max_length=36, primary_key=True)
    username = models.CharField(max_length=20, unique=True, db_index=True)
    # icon = models.ForeignKey('Image.image_id', on_delete=models.SET_NULL)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=36)
    last_name = models.CharField(max_length=36)
    status = models.CharField(max_length=10, default='NEW')  # choices=USER_STATUS, default='NEW')
    # email = models.CharField(max_length=50)
    # birthday = models.DateField()
    # facebook = models.CharField(max_length=50)
    # deviceToken = models.CharField(max_length=152)
    # platform = models.CharField(max_length=10, choices=('android', 'ios'))
    # timeCreated = models.DateField(default=timezone.now)
    # timeLastModified = models.DateField(default=timezone.now)

    @classmethod
    def login(cls, username, password, device_token=None, platform=None):
        try:
            q = Identity.objects.get(username=username)
        except ObjectDoesNotExist:
            print 'username not exist'
            return False
        print q.password, password
        return q.password == password

    @classmethod
    def passwordValidate(cls, password):
        # check length
        if len(password) < 8 or len(password) > 20:
            return False

        # check contains lowercase
        lowerCase = False
        for i in range(ord('a'), ord('z') + 1):
            if chr(i) in password:
                lowerCase = True
                break
        if not lowerCase:
            return False
        print 'has lower case'
        # check contains uppercase
        upperCase = False
        for i in range(ord('A'), ord('Z') + 1):
            if chr(i) in password:
                upperCase = True
                break
        if not upperCase:
            return False
        print 'has upper case'

        num = False
        for i in range(ord('0'), ord('9')):
            if chr(i) in password:
                num = True
                break
        if not num:
            return False
        print 'has number'
        return True

    @classmethod
    def create(cls, user_info):
        if not cls.passwordValidate(user_info['password']):
            print 'invalid password', user_info['password']
            return False
        print 'creating', user_info['username'], user_info['password']
        identity = cls(
            username=user_info['username'],
            password=user_info['password'],
            first_name=user_info['first_name'],
            last_name=user_info['last_name'],)
        identity.save()
            # email=user_info['email'],)
        return identity

