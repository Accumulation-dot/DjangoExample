from rest_framework import serializers
from .models import *


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        field = '__all__'


class TagsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        field = '__all__'


class GoodsModelSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=False)
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Goods
        fields = '__all__'


class GoodsEntryModelSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=False)
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Goods
        fields = '__all__'


class EntryOrderModelSerializer(serializers.ModelSerializer):
    goods = GoodsEntryModelSerializer(many=True)

    class Meta:
        model = EntryOrder
        fields = '__all__'


class EntryOrderSummarySerializer(serializers.ModelSerializer):
    # goods = GoodsEntryModelSerializer(many=True)

    class Meta:
        model = EntryOrder
        fields = ('id', 'name', 'number', 'total')


class TagsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '(name)'


class EntryOrderDetailModelSerializer(serializers.ModelSerializer):
    """
    采购信息
    """
    # order = EntryOrderSummarySerializer(many=False)
    good = GoodsModelSerializer(many=False)

    class Meta:
        model = EntryOrderDetail
        fields = ('id', 'order', 'good')


