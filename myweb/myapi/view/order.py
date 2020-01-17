from rest_framework import generics
from django.db import models
from myapi.model.order import *
from myapi.serializer.order import *


class CommodityList(generics.ListCreateAPIView):
    """ Commodity list create """
    queryset = Commodity.objects.all()
    serializer_class = CommoditySerializer


class CommodityDetail(generics.RetrieveUpdateDestroyAPIView):
    """Commodity get update """
    queryset = Commodity.objects.all()
    serializer_class = CommoditySerializer


class TagList(generics.ListCreateAPIView):
    """ Tag list create """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TagDetail(generics.RetrieveUpdateDestroyAPIView):
    """Tag get update"""
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CategoryList(generics.ListCreateAPIView):
    """Category list create"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateAPIView):
    """Category get update"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

