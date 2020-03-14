from rest_framework import generics
from rest_framework import permissions, status
from rest_framework.response import Response

from machine import models
from machine import serializers
#MachineSerializer, RecordSerializer
from tools.tools import CustomPagination


# Create your views here.


class MachineView(generics.ListAPIView):
    pagination_class = CustomPagination
    queryset = models.Machine.objects.all()
    permission_classes = ([permissions.IsAuthenticatedOrReadOnly])
    serializer_class = serializers.MachineSerializer


class RecordView(generics.ListCreateAPIView):
    pagination_class = CustomPagination
    queryset = models.Machine.objects.all()
    permission_classes = ([permissions.IsAuthenticatedOrReadOnly])
    serializer_class = serializers.RecordSerializer

    # def perform_create(self, serializer):
    #     print(self.request.user)
    #     serializer.save(user=self.request.user)


class RecordInfoView(generics.RetrieveUpdateAPIView):
    queryset = models.Record.objects.all()
    serializer_class = serializers.RecordUpdateSerializer

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

# @api_view([])
# def record_list