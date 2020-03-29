from rest_framework import serializers

# ModelSerializer, CharField, SerializerMethodField
from trade.models import Trade, Record, RecordDetail, Sell, Buy, SellRecord, BuyRecord
from trade import models
from user.serializers import user_info_data, user_info_address


class TradeSerializer(serializers.ModelSerializer):
    type_desc = serializers.CharField(source='get_type_display', read_only=True)
    user = serializers.SerializerMethodField(read_only=True)

    status = serializers.ReadOnlyField()

    # status_desc = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = Trade
        fields = '__all__'

    def get_user(self, obj):
        return user_info_data(obj.user)

    def get_status(self, objc):
        records = Record.objects.filter(trade=objc.id, status__in=(1, 3)).count()
        if records is None:
            return 0
        else:
            return


# 出售
class SellSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)

    status_desc = serializers.CharField(source='get_status_display', read_only=True)

    created = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Sell
        exclude = ('id',)

    def get_user(self, obj):
        # return user_info_data(obj.user)
        return user_info_address(obj.user)


class SellRecordSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)

    # status_desc = serializers.CharField(source='get_status_display', read_only=True)

    created = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = models.SellRecord
        fields = '__all__'

    def get_user(self, obj):
        # return user_info_data(obj.user)
        return user_info_address(obj.user)


class SellDetailSerializer(serializers.ModelSerializer):
    # status_desc = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = models.SellDetail
        fields = '__all__'


class BuySerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)

    created = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    status_desc = serializers.ReadOnlyField(source='get_status_display')

    class Meta:
        model = Buy
        exclude = ('id',)

    def get_user(self, obj):
        return user_info_address(obj.user)
        # user_info_data(obj.user)


class BuyRecordSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)

    # status_desc = serializers.CharField(source='get_status_display', read_only=True)

    class Meta:
        model = models.BuyRecord
        fields = '__all__'

    def get_user(self, obj):
        return user_info_data(obj.user)


class TradeBackSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField(read_only=True)
    type = serializers.CharField(source='get_type_display', read_only=True)

    class Meta:
        model = Trade
        fields = '__all__'

    def get_user(self, obj):
        return user_info_data(obj.user)


class TradeRecordSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField(read_only=True)

    status_desc = serializers.CharField(source='get_status_display',
                                        read_only=True)

    class Meta:
        model = Record
        fields = '__all__'

    def get_owner(self, objc):
        return user_info_data(objc.owner)


class RecordDetailSerializer(serializers.ModelSerializer):
    owner = serializers.SerializerMethodField(read_only=True)

    status_desc = serializers.CharField(source='get_status_display',
                                        read_only=True)

    class Meta:
        model = RecordDetail
        fields = '__all__'

    def get_owner(self, objc):
        return user_info_data(objc.owner)


class BuyInformationSerializer(serializers.ModelSerializer):
    seller = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Buy
        exclude = ('id',)

    def get_seller(self, objc):
        record = BuyRecord.objects.filter(buy=objc, status__in=(0, 1, 3))
        return BuyRecordSerializer(record, many=True).data
