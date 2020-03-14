from rest_framework.serializers import ModelSerializer, Serializer

from chains.news.news import News, NewsRecord


class NewsSerializers(ModelSerializer):

    class Meta:
        model = News
        fields = '__all__'


class NewsRecordSerializers(ModelSerializer):

    class Meta:
        model = NewsRecord
        exclude = ('user',)
