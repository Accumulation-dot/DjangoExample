from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from chains.news.news import News, NewsRecord
from chains.news.news_serializers import NewsSerializers, NewsRecordSerializers


class NewsView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class NewsRecordListView(ListCreateAPIView):
    queryset = NewsRecord.objects.all()
    serializer_class = NewsRecordSerializers
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


