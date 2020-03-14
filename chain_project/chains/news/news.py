from django.db import models

from chains.user.user_serializer import User


class News(models.Model):
    title = models.CharField(max_length=60, verbose_name='标题', help_text='标题')
    img = models.CharField(max_length=256, default='', blank=True, verbose_name='图片', help_text='图片')
    url = models.CharField(max_length=256, default='', blank=True, verbose_name='文章链接', help_text='文章链接')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '新闻表'
        verbose_name_plural = verbose_name


class NewsRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', verbose_name='用户信息', help_text='用户id')
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='news', verbose_name='新闻', help_text='新闻id')
    datetime = models.DateTimeField(auto_now=True, verbose_name='时间', help_text='记录的时间')

    def __str__(self):
        return self.user.username + self.news.title

    class Meta:
        verbose_name = '新闻观看记录'
        verbose_name_plural = verbose_name
