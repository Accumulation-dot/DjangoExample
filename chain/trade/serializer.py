from rest_framework import serializers
# ModelSerializer, CharField, SerializerMethodField
from trade.models import Trade, TradeRecord
from user.models import CoinUserInfo
from user.serializer import CoinUserInfoSerializer


class TradeSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='get_type_display', read_only=True)

    class Meta:
        model = Trade
        fields = '__all__'


class TradeBackSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Trade
        exclude = ('type', )

    def get_user(self, obj):
        info = CoinUserInfo.objects.filter(user=obj.user).first()
        return CoinUserInfoSerializer(info).data


class TradeRecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = TradeRecord
        fields = '__all__'
