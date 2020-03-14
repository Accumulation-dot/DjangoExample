from rest_framework import serializers

from myapi.model.commodity import *
from myapi.serializer.base import ImageSerializer


class CategorySerializer(serializers.ModelSerializer):
    """
    Category Serializer
    """

    class Meta:
        model = Category
        exclude = ('created', 'updated',)


class TagSerializer(serializers.ModelSerializer):
    """
    Tag Serializer
    """

    class Meta:
        model = Tag
        exclude = ('created', 'updated',)


class CommoditySerializer(serializers.ModelSerializer):
    """
    Commodity Serializer
    """

    class Meta:
        model = Commodity
        exclude = ('created', 'updated',)
