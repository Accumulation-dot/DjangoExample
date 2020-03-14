from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class BModel(models.Model):
    updated = models.DateTimeField(auto_now=True, verbose_name='最新更新日期', help_text='最新更新日期')
    create = models.DateTimeField(auto_now_add=True, verbose_name='创建日期', help_text='创建日期')

    class Meta:
        abstract = True

