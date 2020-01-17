from django.contrib.auth.models import User
from django.db import models

from myapi.model.base import UUID
from myapi.model.commodity import Commodity


class Seller(UUID):
    """ 进货商 商家的信息 """
    name = models.CharField(max_length=50,
                            verbose_name='商家名', help_text='商家名称')
    nick_name = models.CharField(max_length=50,
                                 verbose_name='商家名称', help_text='商家名称', blank=True, default='')

    class Meta:
        verbose_name = '商家信息'
        verbose_name_plural = verbose_name
        unique_together = ('name', 'nick_name',)


class Order(UUID):
    """商家的订单"""
    title = models.CharField(max_length=50, )
    total = models.FloatField(verbose_name='总价', help_text='订单需要的价格')
    order_num = models.CharField(max_length=50, blank=True, default='')
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, blank=True, default='',
                               verbose_name='卖家', help_text='卖家的订单')
    commodity_list = models.ManyToManyField(to=Commodity, through='OrderInfo',
                                            through_fields=('order', 'commodity'),
                                            verbose_name='订单的商品信息', help_text='订单内所有的商品的信息')

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name


class UserOrder(UUID):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name='订单用户名', help_text='订单信息用户名')
    total = models.FloatField(verbose_name='总价', help_text='订单需要的价格')
    order_num = models.CharField(max_length=50, blank=True, default='')
    commodity_list = models.ManyToManyField(to=Commodity, through='UserOrderInfo',
                                            through_fields=('order', 'commodity'),
                                            verbose_name='订单的商品信息', help_text='订单内所有的商品的信息')

    class Meta:
        verbose_name = '用户订单'
        verbose_name_plural = verbose_name


class OrderInfo(UUID):
    """ 订单的信息 """
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              verbose_name='订单ID', help_text='订单的ID')
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE,
                                  verbose_name='商品ID', help_text='商品的ID')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0, blank=True,
                                verbose_name='价格', help_text='商品价格')
    num = models.PositiveSmallIntegerField(default=1, blank=True,
                                           verbose_name='商品数量', help_text='商品的数量')

    class Meta:
        verbose_name = '订单详情'
        verbose_name_plural = verbose_name


class UserOrderInfo(UUID):
    """ 订单的信息 """
    order = models.ForeignKey(UserOrder, on_delete=models.CASCADE,
                              verbose_name='订单ID', help_text='订单的ID')
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE,
                                  verbose_name='商品ID', help_text='商品的ID')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0, blank=True,
                                verbose_name='价格', help_text='商品价格')
    num = models.PositiveSmallIntegerField(default=1, blank=True,
                                           verbose_name='商品数量', help_text='商品的数量')

    class Meta:
        verbose_name = '订单详情'
        verbose_name_plural = verbose_name