# !/usr/bin/python3
# -*- coding:utf-8 -*-

from django.db import models


class Test(models.Model):
    title = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '测试'
        verbose_name_plural = verbose_name
