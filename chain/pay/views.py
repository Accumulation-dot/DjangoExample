from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions


from pay import models as pm, serializers as ps
# Create your views here.
from tools.permissions import Owned
from tools.tools import CustomPagination


class PayView(generics.ListCreateAPIView):
    """
    list 查询所有
    create 创建
    """
    queryset = pm.Pay.objects.all()
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = ps.PaySerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        return pm.Pay.objects.filter(user=self.request.user, use=True)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PayDetailView(generics.RetrieveUpdateAPIView):
    """
    获取信息 int:pk

    """
    queryset = pm.Pay.objects.all()
    permission_classes = (permissions.IsAuthenticated, Owned)
    serializer_class = ps.PaySerializer




