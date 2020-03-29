import time
import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from tools.base import BaseModel


def address():
    t = time.time()
    return uuid.uuid5(uuid.NAMESPACE_DNS, str(uuid.uuid1()) + str(int(t)))


class CoinUser(AbstractUser):
    qq = models.CharField('qq 号码', max_length=20, blank=True)
    wechat = models.CharField('微信号码', max_length=40, blank=True)
    level = models.PositiveSmallIntegerField(default=1, choices=((0, '管理员'), (1, '普通用户')),
                                             verbose_name='等级', help_text='等级')

    class Meta:
        verbose_name = verbose_name_plural = '用户表'


class CoinUserInfo(BaseModel):
    user = models.OneToOneField(CoinUser, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=20, blank=True, default='',
                            verbose_name='用户名称', help_text='用户名称 需要完善信息')
    address = models.CharField(max_length=100, blank=False, default=address(),
                               verbose_name='地址', help_text='地址')

    class Meta:
        verbose_name = verbose_name_plural = "用户信息表"


class Identifier(models.Model):
    user = models.OneToOneField(CoinUser, on_delete=models.DO_NOTHING,
                                verbose_name='用户信息', help_text='用户信息')
    name = models.CharField(max_length=20,
                            verbose_name='姓名', help_text='用户信息')
    number = models.CharField(max_length=20,
                              verbose_name='ID', help_text='用户身份证信息')

    class Meta:
        verbose_name = verbose_name_plural = '身份证信息'


def user_info_creation(user):
    info = CoinUserInfo(user=user, name=user.username)
    info.save()
    return info
