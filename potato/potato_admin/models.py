from django.db import models
import time
# Create your models here.


class CreateOptions(models.Model):
    """
    虚基类 (last_update, create, )
    """

    last_update = models.DateTimeField(auto_now=True,
                                       verbose_name='最新更新日期', help_text='最新的更新日期')
    create = models.DateTimeField(auto_now_add=True,
                                  verbose_name='创建日期', help_text='创建日期')

    class Meta:
        abstract = True


class User(CreateOptions):
    """
    用户表
    """
    gender = (
        ('male','男'),
        ('female','女'),
    )
    name = models.CharField(max_length=128, unique=True, verbose_name='用户名', help_text='唯一的用户名 不可以重复')
    password = models.CharField(max_length=256, verbose_name='密码')
    email = models.EmailField(unique=True, verbose_name='邮箱')
    sex = models.CharField(max_length=32, choices=gender, default='男')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class Seller(CreateOptions):
    """
    供货商信息
    """
    name = models.CharField(verbose_name='商家名称', max_length=100, help_text='卖家名称')
    title = models.CharField(verbose_name='卖家会员名', max_length=100, help_text='卖家会员名', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '供货商'
        verbose_name_plural = verbose_name
        unique_together = ('name', 'title',)


class Tags(CreateOptions):
    """
    产品 标签
    """
    title = models.CharField(max_length=30,
                             verbose_name='标题', help_text='显示的标题')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '标记'
        verbose_name_plural = verbose_name


class Category(CreateOptions):
    """
    分类
    """
    title = models.CharField(max_length=30,
                             verbose_name='分类名称', help_text='分类显示')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name


class Commodity(CreateOptions):
    """
    商品的信息
    """
    title = models.CharField(max_length=60,
                             verbose_name='标题', help_text='商品标题')
    sid = models.CharField(max_length=40,  blank=True,
                           verbose_name='货号', help_text='商品货号')
    tag = models.ManyToManyField(Tags, blank=True,
                                 verbose_name='标签', help_text='标签')
    category = models.ForeignKey(Category, blank=True, on_delete=models.CASCADE,
                                 verbose_name='分类', help_text='分类描述')

    price = models.DecimalField(max_digits=8, decimal_places=2, default=2000,
                                verbose_name='价格', help_text='标价')

    # buy_price = models.ManyToManyField(PurchaseOrder,
    #                                    through='PurchaseOrderPrice', through_fields=('commodity', 'order'),
    #                                    verbose_name='买入价格', help_text='根据订单获取买入价格')

    discount = models.PositiveSmallIntegerField(verbose_name='折扣', help_text='折扣', default=100)

    desc = models.CharField(max_length=100, blank=True,
                            verbose_name='描述', help_text='商品的介绍信息')

    def __str__(self):
        return self.title + '商品号' + self.sid

    class Meta:
        verbose_name = '商品信息'
        verbose_name_plural = verbose_name


class PurchaseOrder(CreateOptions):
    """
    进货单
    """
    title = models.CharField(max_length=100,
                             verbose_name='订单标题', help_text='订单的标题，显示的名称')
    num = models.CharField(max_length=100, default=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                           verbose_name='订单号', help_text='订单号，如果没有订单号的时候会默认设置成日期')
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, blank=True,
                               verbose_name='商家信息', help_text='商家信息')
    total = models.DecimalField(max_digits=8, decimal_places=2,
                                verbose_name='金额', help_text='订单支付金额')

    commodities = models.ManyToManyField(to=Commodity,
                                         through='PurchaseOrderPrice', through_fields=('order', 'commodity'))

    def __str__(self):
        return self.title + '  ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    class Meta:
        verbose_name = '进货单'
        verbose_name_plural = verbose_name


class PurchaseOrderPrice(CreateOptions):
    """
    进货单价格
    """
    order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE,
                              verbose_name='order 外键', help_text='订单的外键')
    commodity = models.ForeignKey(Commodity, on_delete=models.CASCADE,
                                  verbose_name='商品编码', help_text='商品的外键')
    price = models.DecimalField(max_digits=8, decimal_places=2,
                                verbose_name='价格', help_text='进货单的价格')
    num = models.PositiveSmallIntegerField(verbose_name='数量 个/套', help_text='货物的数量')

    def __str__(self):
        return '订单号' + self.order.title + '商品名' + self.commodity.title

    class Meta:
        verbose_name = '订单价格信息'
        verbose_name_plural = verbose_name

