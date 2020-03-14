from django.db import models

from user.models import CoinUser


# Create your models here.
class CoinGainRecord(models.Model):
    coin_number = models.FloatField(verbose_name='分数', help_text='获取的分数')
    reason = models.CharField(max_length=100,
                              verbose_name='获取途径', help_text='获取途径')
    datetime = models.DateTimeField(auto_now=True,
                                    verbose_name='获取日期时间', help_text='获取的日期时间')

    class Meta:
        verbose_name = verbose_name_plural = '获取记录表'


trade_status = ((0, '默认状态'), (1, '待付款'), (2, '取消'), (3, '完成'), (4, '删除'))


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


class TradeRecord(models.Model):
    trade = models.ForeignKey(Trade, related_name='交易信息', on_delete=models.CASCADE,
                              verbose_name='交易信息', help_text='交易信息')
    owner = models.ForeignKey(CoinUser, related_name='提交者', on_delete=models.CASCADE,
                              verbose_name='提交者', help_text='出售者')
    datetime = models.DateTimeField(auto_now=True, verbose_name='交易时间', help_text='交易时间')
    status = models.PositiveSmallIntegerField(choices=trade_status, default=1,
                                              verbose_name='状态', help_text='状态')

    class Meta:
        verbose_name = verbose_name_plural = '交易记录'

