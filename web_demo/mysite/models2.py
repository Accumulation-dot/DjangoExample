# !/usr/bin/python3
# -*- coding:utf-8 -*-
import uuid

from django.db import models


# Create your models here.


class CreateOptions(models.Model):
    """
    虚基类 (last_update, create, )
    """
    model_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False,
                                verbose_name='model id', help_text='唯一的id')
    name = models.CharField(max_length=50,
                            verbose_name='名称', help_text='名称信息')
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name='最新更新日期', help_text='最新的更新日期')
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='创建日期', help_text='创建日期')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Category1(CreateOptions):
    class Meta:
        verbose_name = '类别1'
        verbose_name_plural = verbose_name
