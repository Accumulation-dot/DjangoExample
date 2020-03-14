import json

from rest_framework import serializers

from advert import models

from user import serializer
from user import models as UM


class ContentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Content
        exclude = ('readers',)

    def get_user(self, objc):
        info = serializer.CoinUserInfoSerializer(UM.CoinUserInfo.objects.filter(user=objc.id).first())
        return info.data


class RecordSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)

    contents = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Record
        fields = '__all__'

    def get_user(self, objc):
        u = UM.CoinUserInfo.objects.filter(user=objc.user)
        info = serializer.CoinUserInfoSerializer(u.first())
        return info.data

    def get_contents(self, objc):
        va = models.Content.objects.filter(content=objc.content)
        print(va.query)
        return ContentSerializer(models.Content.objects.filter(id=objc.content.id).first()).data
