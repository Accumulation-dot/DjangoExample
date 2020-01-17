from rest_framework import generics
from django.db import models
from myapi.model.order import *
from myapi.serializer.order import *


class SellerList(generics.ListCreateAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class SellerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class UserOrderList(generics.ListCreateAPIView):
    queryset = UserOrder.objects.all()
    serializer_class = UserOrderSerializer


class UserOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserOrder.objects.all()
    serializer_class = UserOrderSerializer


class OrderInfoList(generics.ListCreateAPIView):
    queryset = OrderInfo
    serializer_class = OrderInfoSerializer


class OrderInfoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderInfo
    serializer_class = OrderInfoSerializer
