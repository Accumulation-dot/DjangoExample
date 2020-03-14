from django.contrib.auth.models import User
from django.db import models


class Machine(models.Model):
    title = models.CharField(max_length=30, unique=True, verbose_name='标题', help_text='展示的标题')
    calculate = models.FloatField(verbose_name='计算能力', help_text='矿机的计算能力')
    rent = models.IntegerField(verbose_name='租金', help_text='租金')
    output = models.FloatField(verbose_name='产出总量', help_text='产出总量')
    limit = models.IntegerField(verbose_name='限制租赁数量', help_text='限制租赁的数量')
    number = models.IntegerField(verbose_name='当前剩余数量', help_text='当前可以租赁的数量')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '矿机数据库'
        verbose_name_plural = verbose_name


class MachineRecord(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, verbose_name='对应矿机的外键', help_text='对应矿机的外键')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='租赁的用户', help_text='租赁用户的ID')

    class Meta:
        verbose_name = '矿机出售列表'
        verbose_name_plural = verbose_name
