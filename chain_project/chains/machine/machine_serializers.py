from rest_framework import serializers

from chains.machine.machine import Machine, MachineRecord


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = '__all__'


class MachineRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MachineRecord
        fields = '__all__'
