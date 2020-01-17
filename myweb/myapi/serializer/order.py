from rest_framework import serializers
from myapi.model.order import *


class CategorySerializer(serializers.ModelSerializer):
    """Category Serializer"""
    class Meta:
        model = Category
        exclude = ('created', 'updated',)


class TagSerializer(serializers.ModelSerializer):
    """ Tag Serializer """
    class Meta:
        model = Tag
        exclude = ('created', 'updated',)


class CommoditySerializer(serializers.ModelSerializer):
    """Commodity Serializer"""
    # category_desc =
    tag = TagSerializer(many=True, required=False)
    category = CategorySerializer(required=False)

    class Meta:
        model = Commodity
        exclude = ('created', 'updated',)




