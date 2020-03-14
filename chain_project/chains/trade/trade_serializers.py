from rest_framework import serializers

from chains.trade.trade import Trading


class TradingSellingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Trading
        exclude = ('type',)
