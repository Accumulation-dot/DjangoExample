from rest_framework import serializers
from .models import *


class EntryOrderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryOrder
        fields = '__all__'


class GoodsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = '__all__'


class TagsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '(name)'

