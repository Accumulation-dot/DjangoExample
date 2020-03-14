from django.db import models

# Create your models here.
from user.models import CoinUser


class Content(models.Model):
    title = models.CharField(max_length=60, verbose_name='标题', help_text='标题')
    img = models.CharField(max_length=256, default='', blank=True, verbose_name='图片', help_text='图片')
    url = models.CharField(max_length=256, default='', blank=True, verbose_name='文章链接', help_text='文章链接')

    readers = models.ManyToManyField(CoinUser, through='Record', related_name='readers')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '新闻表'
        verbose_name_plural = verbose_name


class Record(models.Model):
    user = models.ForeignKey(CoinUser, on_delete=models.CASCADE, related_name='user',
                             verbose_name='用户', help_text='用户ID')
    news = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='news',
                             verbose_name='新闻', help_text='新闻id')
    datetime = models.DateTimeField(auto_now=True,
                                    verbose_name='时间', help_text='记录的时间')

    def __str__(self):
        return self.user.username + self.news.title

    class Meta:
        verbose_name = '新闻观看记录'
        verbose_name_plural = verbose_name

    def validated(self, limit):
        # True 可以进行保存， False 不可以保存
        recorded = Record.objects.filter(user=self.user, news=self.news).count() == 0
        limited = Record.objects.filter(user=self.user, date=self.date).count() < limit
        return recorded and limited
