from rest_framework.serializers import ModelSerializer, SerializerMethodField, DateTimeField

from coins.models import query_coin
from user import models
from user.models import CoinUser, CoinUserInfo


class UserSerializer(ModelSerializer):
    def create(self, validated_data):
        user = CoinUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user

    class Meta:
        model = CoinUser
        exclude = ('level',)


class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = CoinUser
        fields = ('username', 'password',)


class CoinUserInfoSerializer(ModelSerializer):
    coin = SerializerMethodField(read_only=True)

    created = DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = CoinUserInfo
        exclude = ('id', 'user', 'name',)

    def get_coin(self, objc):
        return query_coin(objc.user)


class IdentifierSerializer(ModelSerializer):
    class Meta:
        model = models.Identifier
        exclude = ('id', 'user',)


def user_info_data(user):
    return CoinUserInfoSerializer(CoinUserInfo.objects.filter(user=user).first()).data


def user_info_address(user):
    return CoinUserInfo.objects.filter(user=user).first().address

def user_name(user):
    return user.username
