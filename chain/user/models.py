from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
from rest_framework.permissions import BasePermission


class CoinUser(AbstractUser):
    qq = models.CharField('qq 号码', max_length=20, blank=True)
    wechat = models.CharField('微信号码', max_length=40, blank=True)
    level = models.PositiveSmallIntegerField(default=1, choices=((0, '管理员'), (1, '普通用户')),
                                             verbose_name='等级', help_text='等级')

    class Meta:
        verbose_name = verbose_name_plural = '用户信息表'


class CoinUserInfo(models.Model):
    user = models.ForeignKey(CoinUser, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=20, blank=True, default='', verbose_name='用户名称', help_text='用户名称 需要完善信息')
    coin_number = models.FloatField(default=0.0, verbose_name='用户的积分', help_text='用户积分')
    created = models.DateTimeField(auto_now=True)
    frozen = models.FloatField(default=0.0, verbose_name='用户的积分', help_text='用户积分')
    address = models.CharField(max_length=100, blank=False)

    class Meta:
        verbose_name = verbose_name_plural = '用户数量表'


class LevelPermission(BasePermission):
    message = '等级不够， 请联系管理员'

    def has_permission(self, request, view):
        user = CoinUser.objects.filter(id=request.user.id).first()
        return user and user.level == 1


def user_info_creation(user):
    info = CoinUserInfo(user=user)
    info.save()
    return info
