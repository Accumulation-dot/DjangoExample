from django.db import models
from user import models as UM

# Create your models here.


class Machine(models.Model):
    title = models.CharField(max_length=20, unique=True,
                             verbose_name='标题', help_text='标题')

    count = models.PositiveIntegerField(verbose_name='数量', help_text='数量')

    users = models.ManyToManyField(UM.CoinUser, through='Record')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '矿机表'
        verbose_name_plural = verbose_name


class Record(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, related_name='machine')
    user = models.ForeignKey(UM.CoinUser, on_delete=models.CASCADE, related_name='users')
    datetime = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = '矿机租赁列表'
        verbose_name_plural = verbose_name
