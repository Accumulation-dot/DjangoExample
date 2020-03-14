from django.db import models

from user import models as users


# Create your models here.


class Coin(models.Model):
    user = models.ForeignKey(users.CoinUser, on_delete=models.CASCADE, verbose_name='用户ID',
                             help_text='用户ID')
    coin1 = models.FloatField(default=0, verbose_name='币种1')
    coin2 = models.FloatField(default=0, verbose_name='币种2')

    class Meta:
        verbose_name = '货币中心'
        verbose_name_plural = verbose_name


class Record(models.Model):
    user = models.ForeignKey(users.CoinUser, on_delete=models.CASCADE,
                             verbose_name='用户ID', help_text='用户ID')
    # 可以是正可以是负 正表示收入 负表示支出
    point = models.FloatField(verbose_name='获取的数量')
    datetime = models.DateTimeField(auto_now=True)
    desc = models.CharField(max_length=120, default='', null=False,
                            verbose_name='说明', help_text='说明')

    class Meta:
        verbose_name = '货币获取的记录'
        verbose_name_plural = verbose_name


def register_record(user, point=1):
    record = Record(user=user, point=point, desc='注册奖励')
    record.save()
    while True:
        info = users.CoinUserInfo.objects.filter(user=user.id).first()
        num = info.coin_number
        result = users.CoinUserInfo.objects.filter(user=user.id, coin_number=num).update(coin_number=num+point)
        if result == 0:
            continue
        break
    return record


freq_choices = ((0, '有限次数'), (1, '每天次数'), (2, '每月的次数'), (3, '每年的次数'), (4, '未限制次数'))


class Award(models.Model):
    key = models.CharField(max_length=50, unique=True, verbose_name='奖励的key', help_text='奖励的key 根据key进行搜索是否有存在')
    coins = models.FloatField(verbose_name='奖励的分数', help_text='奖励或者需要扣除')
    type = models.IntegerField(verbose_name='奖励的类型', help_text='奖励的类型')
    freq = models.IntegerField(choices=freq_choices, default=0, verbose_name='频率', help_text='频率')
    freq_num = models.IntegerField(default=1, verbose_name='次数', help_text='次数')

    class Meta:
        verbose_name = '奖励类型'
        verbose_name_plural = verbose_name

