from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from coins.models import Record
from coins.serializer import RecordSerializer


@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
def record_list(request, format=None):
    usr = request.user
    print(usr)
    if request.method == 'GET':
        #  owned = 1 获取当前用户下的信息 或者 owned 获取所有
        owned = request.GET.get('owned', '0')
        if owned == '1':
            records = Record.objects.filter(user=usr.id)
        else:
            records = Record.objects.all()
        serializer = RecordSerializer(records, many=True)
        return Response(serializer.data)
