from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from news.models import Content, Record
from user.serializer import user_info_data


class ContentSerializer(ModelSerializer):

    class Meta:
        model = Content
        # fields = '__all__'
        exclude = ('readers', )


class RecordSerializer(ModelSerializer):

    class Meta:
        model = Record
        exclude = ('user',)


class RecordDetailSerializer(ModelSerializer):
    user = SerializerMethodField(read_only=True)

    news = SerializerMethodField(read_only=True)

    class Meta:
        model = Record
        fields = '__all__'

    def get_user(self, obj):
        return user_info_data(obj.user)

    def get_news(self, obj):
        return ContentSerializer(Content.objects.filter(news=obj.news.id).first()).data