from rest_framework.serializers import ModelSerializer

from coins.models import Coin, Record


class CoinSerializer(ModelSerializer):

    class Meta:
        model = Coin
        fields = '__all__'


class RecordSerializer(ModelSerializer):

    class Meta:
        model = Record
        fields = '__all__'
