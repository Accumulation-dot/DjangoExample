from datetime import datetime

from django.db.models import Sum
from rest_framework.serializers import ModelSerializer

from coins.models import Coin, Record, Award


class CoinSerializer(ModelSerializer):

    class Meta:
        model = Coin
        fields = '__all__'


class RecordSerializer(ModelSerializer):

    class Meta:
        model = Record
        fields = '__all__'


class AwardSerializer(ModelSerializer):

    class Meta:
        model = Award
        fields = '__all__'

