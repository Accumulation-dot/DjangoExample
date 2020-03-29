from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from coins.models import Record as CRecord
from coins.models import query_coin, query_rule
from tools.permissions import UnOwned, Owned
from tools.tools import CustomPagination
from trade import models
from trade.models import Trade, Record, item_code, Sell, Buy
from trade.serializer import TradeSerializer, TradeBackSerializer, TradeRecordSerializer, SellSerializer, BuySerializer, \
    SellRecordSerializer, SellDetailSerializer, BuyRecordSerializer, BuyInformationSerializer


# 出售 需要进行校验等等


# 获取别人的出售订单
@api_view(['GET'])
@permission_classes([UnOwned, IsAuthenticated])
def sell_list(request, format=None):
    sells = Sell.objects.filter(status=0).exclude(user=request.user).order_by('-date')
    pagination = CustomPagination()
    query = pagination.paginate_queryset(sells, request)
    if query:
        return pagination.get_paginated_response(SellSerializer(query, many=True).data)
    return pagination.get_paginated_response([])


# 获取自己的订单 出售
@api_view(['GET'])
@permission_classes([Owned])
def sell_mine(request, format=None):
    trades = Sell.objects.filter(status=0).order_by('-date')
    pagination = CustomPagination()
    query = pagination.paginate_queryset(trades, request)
    if query:
        return pagination.get_paginated_response(SellSerializer(query, many=True).data)
    return pagination.get_paginated_response([])


# 发布自己的出售订单
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def sell_item(request, format=None):
    print(request.data)
    serializer = SellSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    # trade = serializer.instance
    # print(request.POST)
    number = request.data.get('number')
    if number is None:
        return Response('必须填写数量才能进行发布')
    coin = query_coin(request.user)
    rule = query_rule()
    cash = float(number) * (1.0 + min(1.0, max(0.0, rule.tax)))
    # print(rule.minus[0].to_python())
    if cash > coin - rule.min_num:
        # float(rule.minus[0]):
        return Response(data='你当前的币不足， 请保证售卖之后还能保留最少{}个币'.format(str(rule.minus)), status=status.HTTP_200_OK)
    serializer.save(user=request.user)
    CRecord(user=request.user, key='selling', point=float(number), desc='挂单出售').save()
    return Response(serializer.data)


# 收购API
@api_view(['GET', ])
@permission_classes([UnOwned, IsAuthenticated])
def buy_list(request, format=None):
    buys = Buy.objects.filter(status=0).exclude(user=request.user).order_by('-date')
    pagination = CustomPagination()
    query = pagination.paginate_queryset(buys, request)
    if query:
        return pagination.get_paginated_response(BuySerializer(query, many=True).data)
    return pagination.get_paginated_response([])


# 我的收购API
@api_view(['GET', ])
@permission_classes([Owned])
def buy_mine(request, format=None):
    buys = Buy.objects.filter(status=0).order_by('-date')
    pagination = CustomPagination()
    query = pagination.paginate_queryset(buys, request)
    if query:
        return pagination.get_paginated_response(BuySerializer(query, many=True).data)
    return pagination.get_paginated_response([])


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def buy_item(request, format=None):
    if request.method == 'POST':
        trade = BuySerializer(data=request.data)
        trade.is_valid(raise_exception=True)
        obj = trade.save(user=request.user)
        return Response(TradeBackSerializer(obj).data)
    else:
        serial_no = request.GET.get('s_no', '')
        if not serial_no:
            return Response('你必须填写要查询的订单')
        buy = Buy.objects.filter(serial_no=serial_no).first()
        if buy is None:
            return Response('不存在的订单号', status=status.HTTP_404_NOT_FOUND)
        return Response(BuyInformationSerializer(buy).data)


# 预定订单
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def sell_item_order(request, format=None):
    serial_no = request.data.get('s_no')
    if serial_no is None:
        return Response('需要提供订单号')
    sell = models.Sell.objects.filter(serial_no=serial_no, status=0).first()
    if sell is None:
        return Response('不存在的订单或订单已被预定')
    if sell.user == request.user:
        return Response('请选择其他的订单')
    data = {'sell': sell.id}
    serializer = SellRecordSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    result = models.Sell.objects.filter(serial_no=serial_no, status=0).update(status=1)
    if result == 0:
        return Response('请刷新重试')
    serializer.save(user=request.user)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


# 填写付款信息 s_no 订单号 ali 支付订单号 预定订单信息
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def sell_item_fill(request, format=None):
    serial_no = request.data.get('s_no')
    ali = request.data.get('order')
    if serial_no is None or ali is None:
        return Response('请输入完整的信息：订单编号和支付订单号码')
    sell = models.SellRecord.objects.filter(serial_no=serial_no, user=request.user, status=0).first()
    if sell is None:
        return Response('不存在的订单或订单已被预定')
    serializer = SellDetailSerializer(data={'record': sell.id, 'order': ali})
    serializer.is_valid(raise_exception=True)
    result = models.SellRecord.objects.filter(serial_no=serial_no, user=request.user, status=0).update(status=1)
    if result == 0:
        return Response('更新失败，请刷新后重试')
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


# 取消预定订单 订单号为预定的订单号
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def sell_item_cancel(request, format=None):
    serial_no = request.data.get('s_no')
    record = models.SellRecord.objects.filter(serial_no=serial_no, ).first()
    if record.status == 0 or record.status == 1:
        result = models.SellRecord.objects.filter(serial_no=serial_no, status=record.status).update(status=2)
        if result == 0:
            return Response('订单取消发生错误')
        return Response('取消成功')
    else:
        return Response('当前状态不能取消')


# 确定订单， 订单号码为原始订单号码
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def sell_item_confirm(request, format=None):
    serial_no = request.data.get('s_no')
    sell = models.Sell.objects.filter(serial_no=serial_no, status=1).first()
    if sell is None:
        return Response('请保证当前订单已付款或者重新刷新当前状态')
    result = models.Sell.objects.filter(serial_no=serial_no, status=sell.status).update(status=3)
    record = models.SellRecord.objects.filter(sell=sell, status=1).first()
    if result == 0:
        return Response('订单确认发生错误')
    CRecord(point=sell.sell.number, key='buy from others', user=record.user).save()
    return Response('确认成功')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def buy_item_order(request, format=None):
    serial_no = request.data.get('s_no')
    if serial_no is None:
        return Response('需要提供订单号')

    buy = models.Buy.objects.filter(serial_no=serial_no, status=0).first()
    if not buy:
        return Response('当前订单号已被预定或不存在, 请选择其他的订单')
    if buy.user == request.user:
        return Response('请选择其他不属于你的订单')
    coin = query_coin(request.user)
    rule = query_rule()
    cash = float(buy.number) * (1.0 + min(1.0, max(0.0, rule.tax)))
    # print(rule.minus[0].to_python())
    # if cash > coin - rule.min_num:
    #     # float(rule.minus[0]):
    #     return Response(data='你当前的币不足， 请保证售卖之后还能保留最少{}个币'.format(str(rule.min_num)))
    data = {'buy': buy.id}
    serializer = BuyRecordSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    result = models.Buy.objects.filter(serial_no=serial_no, status=0).update(status=1)
    if result == 0:
        return Response('请刷新重试')
    serializer.save(user=request.user)
    CRecord(user=request.user, key='selling', point=float(cash) * -1, desc='出售给其他人', ).save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


# 针对预定的订单进行
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def buy_item_fill(request, format=None):
    serial_no = request.data.get('s_no')



# 下订单
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def sell_order(request, format=None):
    item_num = request.POST.get('num')
    # 查询订单是否存在
    if item_num is None:
        return Response('不存在的订单号')
    sell = Sell.objects.filter(serial_no=item_num).first()

    # 查询是否有预定的订单
    count = models.SellRecord.objects.filter(status__in=(0, 1, 3), sell=sell).count()
    if count > 0:
        return Response('当前订单已经被人占用或完成')
    serial = SellSerializer(data=models.SellRecord(sell=sell))
    serial.is_valid(raise_exception=True)
    serial.save(user=request.user)
    return Response(serial.data, status=status.HTTP_201_CREATED)


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
    records = Record.objects.filter(owner=request.user)
    return Response(TradeRecordSerializer(records, many=True).data)


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated, ])
def trade_record(request, pk, format=None):
    record = Record.objects.filter(pk=pk).first()
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


# trade 为出售订单 需要买家填写用户信息
@api_view(['POST'])
@permission_classes([IsAuthenticated, ])
def trade_record_create(request, format=None):
    # 填写信息
    data = request.data
    trade_id = data['trade']
    ti = Trade.objects.filter(id=trade_id).first()
    if ti is None:
        return Response('交易信息不存在', )
    if ti.user == request.user:
        return Response('此订单是你发布的', )
    rs = Record.objects.filter(trade=trade_id)
    if rs.count():
        return Response('已经被预定', )
    record = TradeRecordSerializer(data=data)
    record.is_valid(raise_exception=True)
    while True:
        # 更新
        trade = Trade.objects.filter(id=trade_id).first()
        record.save(owner=request.user)
    return Response(record.data, status=status.HTTP_201_CREATED)


@api_view(["POST"])
@permission_classes([AllowAny, ])
def trade_record_fill(request, format=None):
    # data = request.data
    return Response(item_code())


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def trade_confirm(request, format=None):
    trade = Trade
    return Response('confirm success', )


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def buy_item_info(request, uuid, format=None):
    buy = Buy.objects.filter(serial_no=uuid).first()
    if not buy:
        return Response('不存在的订单号', status=status.HTTP_404_NOT_FOUND)
    return Response(BuyInformationSerializer(buy).data)
