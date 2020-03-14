from rest_framework import serializers

from myapi.model.order import *


class SellerSerializer(serializers.ModelSerializer):
    """
    卖家信息
    """
    class Meta:
        model = Seller
        exclude = ('created', 'updated',)


class OrderSerializer(serializers.ModelSerializer):
    """
    订单
    """
    class Meta:
        model = Order
        exclude = ('created', 'updated',)


class OrderInfoSerializer(serializers.ModelSerializer):
    """
    订单信息
    """
    class Meta:
        model = OrderInfo
        exclude = ('updated',)


class UserOrderSerializer(serializers.ModelSerializer):
    """
    用户订单
    """
    class Meta:
        model = UserOrder
        exclude = ('created', 'updated',)


class UserOrderInfoSerializer(serializers.ModelSerializer):
    """
    用户订单详情
    """
    class Meta:
        model = UserOrderInfo
        exclude = ('created', 'updated',)

