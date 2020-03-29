from rest_framework import generics
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from machine import models
from machine import serializers
# MachineSerializer, RecordSerializer
from tools.tools import CustomPagination
from tools.permissions import Owned


# Create your views here.


class MachineView(generics.ListAPIView):
    pagination_class = CustomPagination
    queryset = models.Machine.objects.all()
    permission_classes = ([permissions.IsAuthenticatedOrReadOnly])
    serializer_class = serializers.MachineSerializer


class RecordView(generics.ListCreateAPIView):
    pagination_class = CustomPagination
    queryset = models.Machine.objects.all()
    permission_classes = ([permissions.IsAuthenticatedOrReadOnly, ])
    serializer_class = serializers.RecordSerializer


class RecordInfoView(generics.RetrieveUpdateAPIView):
    queryset = models.Record.objects.all()
    serializer_class = serializers.RecordUpdateSerializer
    permission_classes = ([permissions.IsAuthenticated, Owned])
