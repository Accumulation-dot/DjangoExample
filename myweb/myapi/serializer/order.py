from rest_framework import serializers

from myapi.model.order import *


class SellerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        exclude = ('created', 'updated',)


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        exclude = ('created', 'updated',)


class OrderInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderInfo
        exclude = ('updated',)


class UserOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserOrder
        exclude = ('created', 'updated',)
