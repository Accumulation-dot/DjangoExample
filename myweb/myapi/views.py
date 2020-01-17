from django.shortcuts import render
from rest_framework.response import Response
import rest_framework.status as rf_status
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from django.db import models
# Create your view here.
from myapi.serializer.serializers import *
from .model.order import *
from .models import *

from django.contrib.auth import logout
from django.views.generic import TemplateView, CreateView, RedirectView, ListView, FormView, UpdateView, DeleteView

from rest_framework import generics

"""
class UserView(APIView):
    renderer_classes = [JSONRenderer]
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        user = UserSerializer(data=request.data)
        if user.is_valid():

            user.save()
            # info = UserInformation()
            # info.save_with(user)
            # device = UserProfile()
            # device.save_with(user, request)
            return Response(UserSerializer(user).data, status=rf_status.HTTP_201_CREATED)
        return Response(status=rf_status.HTTP_400_BAD_REQUEST)


class UsersView(APIView):
    renderer_classes = [JSONRenderer]
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        u = User.objects.all()
        s = UserSerializer(u, many=True)
        return Response(s.data)

"""


# class CommodityView(APIView):
#     renderer_classes = [JSONRenderer]
#     authentication_classes = []
#     permission_classes = []
#
#     def get(self, request, format=None):
#         commodities = Commodity.objects.all()
#         serializer = CommoditySerializer(commodities, many=True)
#         return Response(serializer.data)
#
#
# class CategoryView(APIView):
#     renderer_classes = [JSONRenderer]
#     authentication_classes = []
#     permission_classes = []
#
#     def get(self, request, format=None):
#         categories = Category.objects.all()
#         serializer = CategorySerializer(categories, many=True)
#         return Response(serializer.data)
#
#
# class CategoryGList(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


