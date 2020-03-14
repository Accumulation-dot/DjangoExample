from rest_framework.serializers import ModelSerializer

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
    class Meta:
        model = CoinUserInfo
        exclude = ('id', 'user')


def user_info_data(user):
    return CoinUserInfoSerializer(CoinUserInfo.objects.filter(user=user).first()).data