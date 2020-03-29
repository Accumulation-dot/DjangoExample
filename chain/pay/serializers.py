from rest_framework import serializers

from pay import models

from user import models as um

from user import serializers as us


class PaySerializer(serializers.ModelSerializer):
    """
    支付的序列类
    """
    type_desc = serializers.ReadOnlyField(source='get_type_display')

    # user = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Pay
        exclude = ('user', 'created',)

    def get_user(self, objc):
        return us.user_info_address(objc.user)


class UserPaySerializer(serializers.ModelSerializer):

    pays = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = um.CoinUserInfo
        exclude = ('created',)

    def get_pays(self, obj):
        return PaySerializer(models.Pay.objects.filter(user=obj.user, use=True), many=True).data