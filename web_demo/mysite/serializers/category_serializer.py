# !/usr/bin/python3
# -*- coding:utf-8 -*-

from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        field = '__all__'
