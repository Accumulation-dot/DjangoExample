from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from trade.models import Trade, TradeRecord
from trade.serializer import TradeSerializer, TradeBackSerializer, TradeRecordSerializer
# from rest_framework.views import


# 出售 需要进行校验等等
@api_view(['GET', 'POST', ])
@permission_classes([IsAuthenticated, ])
def sell_list(request, format=None):
    if request.method == 'GET':
        trades = Trade.objects.filter(type=1, status=0)
        serializer = TradeSerializer(trades, many=True)
        return Response(serializer.data)
    else:
        data = request.data
        data['user'] = request.user.id
        data['type'] = 1
        record = TradeSerializer(data=data)
        record.is_valid(raise_exception=True)
        record.save()
        return Response(record.data)


# 收购API
@api_view(['GET', 'POST', ])
@permission_classes([IsAuthenticated, ])
def buy_list(request, format=None):
    if request.method == 'GET':
        trades = Trade.objects.filter(type=2)
        serializer = TradeSerializer(trades, many=True)
        return Response(serializer.data)
    else:
        data = request.data
        data['user'] = request.user.id
        data['type'] = 2
        trade = TradeSerializer(data=data)
        if trade.is_valid():
            obj = trade.save()
            return Response(TradeBackSerializer(obj).data)
        return Response(data='Bad request', status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated, ])
def trade_item(request, pk, format=None):
    if request.method == 'GET':
        trades = Trade.objects.filter(pk=pk).first()
        serializer = TradeSerializer(trades, many=False)
        return Response(serializer.data)
    else:
        return Response('', status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated, ])
def records(request, format=None):
    records = TradeRecord.objects.filter(owner=request.user)
    return Response(TradeRecordSerializer(records, many=True).data)


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated, ])
def trade_record(request, pk, format=None):
    record = TradeRecord.objects.filter(pk=pk).first()
    if record is None:
        return Response('不存在的节点', status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = TradeRecordSerializer(record)
        return Response(serializer.data)
    else:
        serializer = TradeRecordSerializer(instance=record, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def trade_record_create(request, format=None):
    data = request.data
    data['owner'] = request.user.id
    record = TradeRecordSerializer(data=data)
    record.is_valid(raise_exception=True)
    record.save()
    return Response(record.data)
