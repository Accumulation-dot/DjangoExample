# !/usr/bin/python3
# -*- coding:utf-8 -*-

from .models import *
from rest_framework import serializers

"""
class Category1Serializer(serializers.ModelSerializer):

    class Meta:
        model = Category1
        fields = '__all__'


class Category2Serializer(serializers.ModelSerializer):

    class Meta:
        model = Category2
        fields = '__all__'


class Category3Serializer(serializers.ModelSerializer):

    class Meta:
        model = Category3
        fields = '__all__'


class Category4Serializer(serializers.ModelSerializer):

    class Meta:
        model = Category4
        fields = '__all__'
"""

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'
