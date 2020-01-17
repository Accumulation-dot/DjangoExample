from django.contrib.auth.models import User
from django.db import models
from django.utils.html import format_html
from myapi.model.seller import Seller
from myapi.models import Creation, UUID


class Tag(Creation):
    """标签表 可以添加 便于查看"""
    title = models.CharField(max_length=30, unique=True,
                             verbose_name='标题', help_text='标题')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '标签表'
        verbose_name_plural = verbose_name


class Image(Creation):
    url = models.ImageField(upload_to='img', default='', blank=True, null=True,
                            verbose_name='图片', help_text='展示的图片')

    def __str__(self):
        return self.img_display()

    def img_display(self):
        return format_html(
            '<img src="{}" width="15px"></img>',
            self.url.url,
        )

    class Meta:
        verbose_name = '图片表'
        verbose_name_plural = verbose_name


class Category(Creation):
    """分类表 不同分类便于分类搜索"""
    title = models.CharField(max_length=30, unique=True,
                             verbose_name='标题', help_text='标题')

    img = models.ImageField(upload_to='img/c', default='', blank=True, null=True,
                            verbose_name='图片', help_text='展示的图片')

    def __str__(self):
        return self.title

    def img_display(self):
        img = ''
        if self.img:
            img = self.img.url
        return format_html(
            '<img src="{}" width="30px"></img>',
            img,
        )

    img_display.short_description = u'图片'

    class Meta:
        verbose_name = '分类表'
        verbose_name_plural = verbose_name


class Commodity(Creation):
    SELLING_STATUS = (
        (0, '售空'),
        (1, '出售中'),
        (2, '补货中'),
    )
    title = models.CharField(max_length=30, default='',
                             verbose_name='标题', help_text='标题')
    sub_title = models.CharField(max_length=50, blank=True, default='',
                                 verbose_name='子标题', help_text='子标题')
    price = models.FloatField(verbose_name='价格', help_text='价格', default=0.00)
    status = models.PositiveSmallIntegerField(choices=SELLING_STATUS, default=1)
    qr_code = models.CharField(max_length=20, blank=True, default='',
                               verbose_name='二维码', help_text='二维码标签上的信息如果有的话')
    tag = models.ManyToManyField(Tag, blank=True, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, default=None,
                                 related_name='category_title',
                                 verbose_name='分类', help_text='分类信息')
    # img = models.ImageField(upload_to='img/', default='', blank=True, null=True,
    #                         verbose_name='图片', help_text='展示的图片')
    imgs = models.ManyToManyField(Image, default='',
                                  verbose_name='图片', help_text='图片信息')

    def img_display(self):
        return ''
        #     format_html(
        #     '<img src="{}" width="30px"></img>',
        #     self.imgs.first.url,
        # )

    desc = models.CharField(max_length=100, blank=True, default='',
                            verbose_name='描述', help_text='描述信息')

    def __str__(self):
        return self.title + self.sub_title

    img_display.short_description = u'图片'

    class Meta:
        verbose_name = '商品表'
        verbose_name_plural = verbose_name


class Order(UUID):
    """商家的订单"""
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             verbose_name='订单用户名', help_text='订单信息用户名')
    title = models.CharField(max_length=50,)
    total = models.FloatField(verbose_name='总价', help_text='订单需要的价格')
    order_num = models.CharField(max_length=50, blank=True, default='')
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, blank=True, default='',
                               verbose_name='卖家', help_text='卖家的订单')
    commodity_list = models.ManyToManyField(to=Commodity, through='OrderInformation',
                                            through_fields=('order', 'commodity'), related_query_name='list',
                                            verbose_name='订单的商品信息', help_text='订单内所有的商品的信息')

    class Meta:
        verbose_name = '订单'
        verbose_name_plural = verbose_name


class OrderInformation(UUID):
    """ 订单的信息 """
    order = models.ForeignKey(Order, on_delete=models.CASCADE,
                              verbose_name='订单ID', help_text='订单的ID')
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE,
                                  verbose_name='商品ID', help_text='商品的ID')
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0, blank=True,
                                verbose_name='价格', help_text='商品价格')
    com_num = models.PositiveSmallIntegerField(default=1, blank=True,
                                               verbose_name='商品数量', help_text='商品的数量')

    class Meta:
        verbose_name = '订单详情'
        verbose_name_plural = verbose_name
