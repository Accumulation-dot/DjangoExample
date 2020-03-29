from rest_framework.serializers import ModelSerializer, SerializerMethodField

from machine import models
from user.serializers import user_info_data


class MachineSerializer(ModelSerializer):
    class Meta:
        model = models.Machine
        exclude = ('users',)


class RecordSerializer(ModelSerializer):

    # user = SerializerMethodField(read_only=True)

    # user = ReadOnlyField(source='user.username')

    # m_info = SerializerMethodField(read_only=True)
    #
    # u_info = SerializerMethodField(read_only=True)

    class Meta:
        model = models.Record
        fields = '__all__'
        # extra_kwargs = {
        #     'context': {'partial': True}
        # }

    # def get_user(self, obj):
    #     info = CoinUser.objects.filter(user=obj.users).first()
    #     return UserRegisterSerializer(info).data

    # def get_m_info(self, obj):
    #     machine = models.Machine.objects.filter(id=obj.machine).first()
    #     return MachineSerializer(machine).data
    #
    # def get_u_info(self, obj):
    #     info = CoinUserInfo.objects.filter(user=obj.user).first()
    #     return CoinUserInfoSerializer(info).data


class RecordUpdateSerializer(ModelSerializer):
    m_info = SerializerMethodField(read_only=True)

    u_info = SerializerMethodField(read_only=True)

    class Meta:
        model = models.Record
        fields = '__all__'
        extra_kwargs = {
            'partial': True
        }

    def get_m_info(self, obj):
        machine = models.Machine.objects.filter(id=obj.machine).first()
        return MachineSerializer(machine).data

    def get_u_info(self, obj):
        return user_info_data(obj.user)
