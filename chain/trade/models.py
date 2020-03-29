import random
import time
import uuid

from django.db import models

from tools.choices import trade_status
from tools import choices
from user.models import CoinUser, CoinUserInfo

from tools.base import BaseModel


def get_order_code():
    return uuid.uuid5(uuid.NAMESPACE_DNS, str(uuid.uuid1()) + str(random.random()))


def item_code(key='1'):
    lime = time.localtime()
    t = time.time()
    return time.strftime("%Y%m%d%H%M%S", lime) + '-' + str(key) + '-' + str(int(t))


# Create your models here.
class CoinGainRecord(models.Model):
    coin_number = models.FloatField(verbose_name='分数', help_text='获取的分数')
    reason = models.CharField(max_length=100,
                              verbose_name='获取途径', help_text='获取途径')
    datetime = models.DateTimeField(auto_now=True,
                                    verbose_name='获取日期时间', help_text='获取的日期时间')

    class Meta:
        verbose_name = verbose_name_plural = '获取记录表'


class Trade(models.Model):
    number = models.FloatField(verbose_name='交易的数量总量')
    # last_number = models.FloatField(verbose_name='剩余量')
    type = models.SmallIntegerField(default=1, choices=((1, '出售'), (2, "收购")),
                                    verbose_name='类型', help_text='类型 1: 出售 2 收购')
    user = models.ForeignKey(CoinUser, on_delete=models.CASCADE,
                             verbose_name='用户', help_text='用户')
    status = models.PositiveSmallIntegerField(verbose_name='状态', help_text='状态',
                                              choices=trade_status, default=0)

    class Meta:
        verbose_name = verbose_name_plural = '交易表'


# 用户出售表
class Sell(BaseModel):
    number = models.FloatField(verbose_name='交易的数量总量')
    user = models.ForeignKey(CoinUser, on_delete=models.CASCADE,
                             verbose_name='用户', help_text='用户')
    status = models.PositiveSmallIntegerField(verbose_name='状态', help_text='状态',
                                              choices=trade_status, default=0)
    serial_no = models.CharField(max_length=50, default=item_code(1))

    price = models.FloatField(default=0, verbose_name='sell_price', help_text='出售单价')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = verbose_name_plural = '出售表'


# 用户收购表
class Buy(BaseModel):
    number = models.FloatField(verbose_name='交易的数量总量')
    user = models.ForeignKey(CoinUser, on_delete=models.CASCADE,
                             verbose_name='用户', help_text='用户')
    status = models.PositiveSmallIntegerField(verbose_name='状态', help_text='状态',
                                              choices=trade_status, default=0)
    serial_no = models.CharField(max_length=50, default=item_code(2))
    price = models.FloatField(default=0, verbose_name='buy_price', help_text='收购单价')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = verbose_name_plural = '收购表'
        ordering = ['date']


class SellRecord(BaseModel):
    user = models.ForeignKey(CoinUser, related_name='buyer', on_delete=models.CASCADE,
                             verbose_name='提交者', help_text='出售者')
    sell = models.ForeignKey(Sell, related_name='sell', on_delete=models.CASCADE,
                             verbose_name='sell', help_text='相关订单')
    status = models.PositiveSmallIntegerField(verbose_name='状态', choices=choices.sell_status, default=0)
    serial_no = models.CharField(max_length=50, default=item_code(3))

    class Meta:
        verbose_name = verbose_name_plural = '出售记录'


class BuyRecord(BaseModel):
    user = models.ForeignKey(CoinUser, related_name='seller', on_delete=models.CASCADE,
                             verbose_name='提交者', help_text='出售者')

    buy = models.ForeignKey(Buy, related_name='buy', on_delete=models.CASCADE,
                            verbose_name='buy', help_text='相关订单')
    status = models.PositiveSmallIntegerField(verbose_name='状态', choices=choices.buy_status, default=0)
    serial_no = models.CharField(max_length=50, default=item_code(4))

    class Meta:
        verbose_name = verbose_name_plural = '出售记录'


class SellDetail(BaseModel):
    record = models.OneToOneField(SellRecord, on_delete=models.CASCADE,
                                  verbose_name='record_id', help_text='出售记录')
    order = models.CharField(max_length=50,)

    class Meta:
        verbose_name = verbose_name_plural = '出售完善的信息'


class BuyDetail(BaseModel):
    record = models.OneToOneField(SellRecord, on_delete=models.CASCADE,
                                  verbose_name='record_id', help_text='出售记录')
    order = models.CharField(max_length=50, )

    class Meta:
        verbose_name = verbose_name_plural = '收购完善的信息'


class Record(models.Model):
    trade = models.ForeignKey(Trade, related_name='交易信息', on_delete=models.CASCADE,
                              verbose_name='交易信息', help_text='交易信息')
    owner = models.ForeignKey(CoinUser, related_name='提交者', on_delete=models.CASCADE,
                              verbose_name='提交者', help_text='出售者')
    datetime = models.DateTimeField(auto_now=True, verbose_name='交易时间', help_text='交易时间')
    status = models.PositiveSmallIntegerField(choices=trade_status, default=1,
                                              verbose_name='状态', help_text='状态')
    record_number = models.CharField(max_length=100, default=get_order_code)

    class Meta:
        verbose_name = verbose_name_plural = '交易记录'


class RecordDetail(models.Model):
    record = models.ForeignKey(Record, related_name='交易记录', on_delete=models.CASCADE)

    ali_order = models.CharField(max_length=100, )

    class Meta:
        verbose_name = verbose_name_plural = '交易记录补充信息'
