import uuid

from django.db import models
from django.utils.html import format_html


class Creation(models.Model):
    """
        updated 更新日期
        created 创建日期
        """
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name='最新更新日期', help_text='最新的更新日期')
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='创建日期', help_text='创建日期')

    class Meta:
        abstract = True


class UUID(Creation):
    """
    使用UUID作为主键的model m_id
    updated 更新时间
    created 创建时间
    """
    u_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False,
                            verbose_name='model id', help_text='唯一的id')

    class Meta:
        abstract = True


class Image(Creation):
    url = models.ImageField(upload_to='img', default='', blank=True, null=True,
                            verbose_name='图片', help_text='展示的图片')

    def __str__(self):
        return self.url

    def img_display(self):
        return format_html(
            '<img src="{}" width="15px"></img>',
            self.url.url,
        )

    img_display.short_description = u'图片'

    class Meta:
        verbose_name = '图像'
        verbose_name_plural = verbose_name

