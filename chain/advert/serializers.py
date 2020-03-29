import json

from rest_framework import serializers

from advert import models

from user import serializers as us
from user import models as um
from user.serializers import user_info_data, user_name


class ContentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    username = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Content
        exclude = ('readers',)

    def get_user(self, objc):
        return user_info_data(objc.user)

    def get_username(self, objc):
        return user_name(objc.user)


class ContentSummary(serializers.ModelSerializer):

    class Meta:
        model = models.Content
        exclude = ('readers', 'user', )


class RecordSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)

    contents = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Record
        fields = '__all__'

    def get_user(self, objc):
        # u = um.CoinUserInfo.objects.filter(user=objc.user)
        # info = us.CoinUserInfoSerializer(u.first())
        return user_info_data(objc.user)

    def get_contents(self, objc):
        return ContentSerializer(models.Content.objects.filter(id=objc.content.id).first()).data
