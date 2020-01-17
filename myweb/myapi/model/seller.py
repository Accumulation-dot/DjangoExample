from django.db import models
from myapi.models import UUID


class Seller(UUID):
    """ 进货商 商家的信息 """
    name = models.CharField(max_length=50,
                            verbose_name='商家名', help_text='商家名称')
    nick_name = models.CharField(max_length=50,
                                 verbose_name='', help_text='', blank=True, default='')

    class Meta:
        verbose_name = '商家信息'
        verbose_name_plural = verbose_name
        unique_together = ('name', 'nick_name',)
