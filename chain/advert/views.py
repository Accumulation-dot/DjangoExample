from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from advert import models as am
from advert import serializers
# Create your views here.
from tools.tools import CustomPagination
from user.models import CoinUser


class ContentView(generics.ListCreateAPIView):
    queryset = am.Content.objects.all()
    pagination_class = CustomPagination
    permission_classes = ([permissions.IsAuthenticatedOrReadOnly])
    serializer_class = serializers.ContentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ContentDetailView(generics.RetrieveAPIView):
    queryset = am.Content.objects.all()
    permission_classes = ([permissions.IsAuthenticatedOrReadOnly])
    serializer_class = serializers.ContentSerializer


class RecordView(generics.ListCreateAPIView):
    queryset = am.Record.objects.all()
    pagination_class = CustomPagination
    permission_classes = ([permissions.IsAuthenticatedOrReadOnly])
    serializer_class = serializers.RecordSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RecordDetailView(generics.RetrieveAPIView):
    queryset = am.Record.objects.all()
    permission_classes = ([permissions.IsAuthenticatedOrReadOnly])
    serializer_class = serializers.RecordSerializer


@api_view(['GET', ])
@permission_classes([permissions.IsAuthenticated, ])
def user_records(request, format=None):
    username = request.GET.get('username', request.user.username)
    # page = request.GET.get('page', '1')
    # size = request.GET.get('size', '30')
    user = CoinUser.objects.filter(username=username).first()
    if user and user.id:
        ads = am.Content.objects.filter(user=user)
        p = CustomPagination()
        query = p.paginate_queryset(ads, request)
        if query:
            return p.get_paginated_response(serializers.ContentSummary(query, many=True).data)
        return p.get_paginated_response([])
    return Response(data='不存在的数据', status=status.HTTP_404_NOT_FOUND)
