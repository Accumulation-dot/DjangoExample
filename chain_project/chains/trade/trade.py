from django.contrib.auth.models import User
from django.db import models


class Trading(models.Model):
    trading_status = (
        ('进行中', 1),
        ('结束', 2)
    )

    trading_type = (
        ('出售', 1),
        ('收购', 2)
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='用户', help_text='用户ID')
    coin = models.FloatField(verbose_name='币数量', help_text='币的数量')
    datetime = models.DateTimeField(auto_now=True, verbose_name='发布日期', help_text='发布时间日期')
    status = models.SmallIntegerField(choices=trading_status, default=1, verbose_name='交易状态', help_text='交易状态')
    type = models.SmallIntegerField(choices=trading_type, default=1, verbose_name='交易类型', help_text='交易类型')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = '出售/收购列表'
        verbose_name_plural = verbose_name


class Trade(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='出售者', verbose_name='出售者',
                               help_text='出售者的ID')
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='收购者', verbose_name='收购者',
                              help_text='收购者的ID')
    point = models.IntegerField(verbose_name='分数', help_text='出售的分数')
    datetime = models.DateTimeField(auto_now=True, help_text='日期时间', verbose_name='日期时间')

    def __str__(self):
        return self.seller.username + '->' + self.buyer.username + self.point

    class Meta:
        verbose_name = '交易记录'
        verbose_name_plural = verbose_name
