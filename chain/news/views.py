from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from rest_framework import generics
from news.models import Content, Record
from news.serializer import ContentSerializer, RecordSerializer, RecordDetailSerializer
from tools.tools import CustomPagination


# @api_view(['GET', 'POST'])
# @permission_classes([AllowAny, ])
# def news_list(request, format=None):
#     if request.method == 'POST':
#         serializer = ContentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         contents = Content.objects.all()
#         serializer = ContentSerializer(contents, many=True)
#         return Response(serializer.data)
#
#
# @api_view(['GET', 'POST'])
# @permission_classes([IsAuthenticated, ])
# def record_list(request, format=None):
#     usr = request.user
#     if request.method == 'GET':
#         #  owned = 1 获取当前用户下的信息 或者 owned 获取所有
#         owned = int(request.GET.get('owned', '0'))
#         if owned == 1:
#             records = Record.objects.filter(user=usr.id)
#         else:
#             records = Record.objects.all()
#         serializer = RecordSerializer(records, many=True)
#         return Response(serializer.data)
#     else:
#         data = request.data
#         data['user'] = usr.id
#         record = RecordSerializer(data=request.data)
#         if record.is_valid():
#             record.save()
#             return Response(record.data)
#         return Response(data='Bad request', status=status.HTTP_400_BAD_REQUEST)


class ContentView(generics.ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    permission_classes = ([IsAuthenticatedOrReadOnly])
    pagination_class = CustomPagination


class RecordView(generics.ListCreateAPIView):
    queryset = Record.objects.all()
    permission_classes = ([IsAuthenticatedOrReadOnly])
    serializer_class = RecordSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RecordDetailView(generics.RetrieveAPIView):
    queryset = Record.objects.all()
    permission_classes = ([IsAuthenticatedOrReadOnly])
    serializer_class = RecordDetailSerializer
