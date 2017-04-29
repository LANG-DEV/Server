# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Identity(models.Model):
    username = models.CharField(max_length=36)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=36)
    last_name = models.CharField(max_length=36)
    status = models.CharField(max_length=10)
