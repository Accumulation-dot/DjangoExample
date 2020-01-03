from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(default='', max_length=30, verbose_name='名称', help_text='类别名称')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '类别'
        verbose_name_plural = verbose_name


class Tags(models.Model):
    name = models.CharField(default='', max_length=30, verbose_name='名称', help_text='标签名称')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name


class Goods(models.Model):
    name = models.CharField(default='',
                            max_length=30,
                            verbose_name='名称',
                            help_text='商品名称')
    desc = models.CharField(default='',
                            max_length=100,
                            verbose_name='商品描述',
                            help_text='商品的介绍')
    category = models.ForeignKey(Category,
                                 default=0,
                                 on_delete=models.CASCADE,
                                 verbose_name='类别',
                                 help_text='所属类别, 默认没有类别')
    tags = models.ManyToManyField(Tags, blank=True)
    price = models.DecimalField(default=0.00,
                                max_digits=8,
                                decimal_places=2,
                                verbose_name='当前定价',
                                help_text='当前的价格')
    snid = models.CharField(blank=True,
                            default=None,
                            max_length=30,
                            verbose_name='商品编码',
                            help_text='商品编码 传说中是唯一的')

    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name


# class BoughtPrice(models.Model):
#     goods = models.ForeignKey(Goods, on_delete=models.CASCADE, default=None)
#     order = models.ForeignKey(EntryOrder, on_delete=models.CASCADE, default=None)
#     price = models.DecimalField(verbose_name='当前价格', max_digits=15, decimal_places=2, help_text='定价')
#     num = models.PositiveSmallIntegerField(verbose_name='购买数量', default=0, help_text='购买货物时候的数量')
#     created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
#
#     def __str__(self):
#         return str(self.price)
#
#     class Meta:
#         verbose_name = '采购价格'
#         verbose_name_plural = verbose_name


class EntryOrder(models.Model):
    name = models.CharField(verbose_name='订单描述', max_length=60, help_text='订单描述', null=False, default='写点啥都行啊')
    number = models.CharField(max_length=60, null=True, verbose_name='订单号码', help_text='订单号码 不一定存在 不存在就是null')
    total = models.DecimalField(verbose_name='总价', help_text='当前订单花费多少钱', max_digits=14, decimal_places=2)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    goods = models.ManyToManyField(Goods, through='EntryOrderDetail', through_fields=('order', 'good'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '进货单'
        verbose_name_plural = verbose_name


class SoldOrder(models.Model):
    name = models.CharField(verbose_name='订单描述',
                            max_length=60,
                            help_text='订单描述',
                            blank=False, default='写点啥都行啊')
    number = models.CharField(max_length=60, blank=True, verbose_name='订单号码', help_text='订单号码 不一定存在 不存在就是null')
    total = models.DecimalField(verbose_name='总价', help_text='当前订单花费多少钱', max_digits=14, decimal_places=2)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    goods = models.ManyToManyField(Goods, through='SoldOrderDetails', through_fields=('order', 'good'))
    # sold_order = models.ManyToManyField(SoldOrder, through='SoldOrderDetails', through_fields=('good', 'order'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '售货单'
        verbose_name_plural = verbose_name


class EntryOrderDetail(models.Model):
    good = models.ForeignKey(Goods, on_delete=models.CASCADE, default=None)
    order = models.ForeignKey(EntryOrder, on_delete=models.CASCADE, default=None)
    price = models.DecimalField(verbose_name='订单内价格', max_digits=8, decimal_places=2)
    num = models.SmallIntegerField(verbose_name='买入的数量 默认为1', default=1)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return self.good.name + str(self.price)

    class Meta:
        verbose_name = '采购价格信息'
        verbose_name_plural = verbose_name


class SoldOrderDetails(models.Model):
    good = models.ForeignKey(Goods, on_delete=models.CASCADE, default=None, help_text='商品的id')
    order = models.ForeignKey(SoldOrder, on_delete=models.CASCADE, default=None, help_text='订单id 可能为空')
    price = models.DecimalField(verbose_name='订单内价格', max_digits=8, decimal_places=2)
    num = models.SmallIntegerField(verbose_name='卖出的数量 默认为1', default=1)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __str__(self):
        return str(self.price) + str(self.created_time)

    class Meta:
        verbose_name = '出售价格信息'
        verbose_name_plural = verbose_name
