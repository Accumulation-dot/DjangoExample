from django.shortcuts import render
from rest_framework import generics, permissions
from advert import models as AM
# Create your views here.
from tools.tools import CustomPagination
from advert import serializers


class ContentView(generics.ListCreateAPIView):
    queryset = AM.Content.objects.all()
    pagination_class = CustomPagination
    permission_classes = ([permissions.IsAuthenticatedOrReadOnly])
    serializer_class = serializers.ContentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ContentDetailView(generics.RetrieveAPIView):
    queryset = AM.Content.objects.all()
    permission_classes = ([permissions.IsAuthenticatedOrReadOnly])
    serializer_class = serializers.ContentSerializer


class RecordView(generics.ListCreateAPIView):
    queryset = AM.Record.objects.all()
    pagination_class = CustomPagination
    permission_classes = ([permissions.IsAuthenticatedOrReadOnly])
    serializer_class = serializers.RecordSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RecordDetailView(generics.RetrieveAPIView):
    queryset = AM.Record.objects.all()
    permission_classes = ([permissions.IsAuthenticatedOrReadOnly])
    serializer_class = serializers.RecordSerializer
