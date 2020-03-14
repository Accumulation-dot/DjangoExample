# Generated by Django 3.0.1 on 2020-01-03 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now=True, help_text='最新的更新日期', verbose_name='最新更新日期')),
                ('create', models.DateTimeField(auto_now_add=True, help_text='创建日期', verbose_name='创建日期')),
                ('title', models.CharField(help_text='分类显示', max_length=30, verbose_name='分类名称')),
            ],
            options={
                'verbose_name': '分类',
                'verbose_name_plural': '分类',
            },
        ),
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now=True, help_text='最新的更新日期', verbose_name='最新更新日期')),
                ('create', models.DateTimeField(auto_now_add=True, help_text='创建日期', verbose_name='创建日期')),
                ('title', models.CharField(help_text='商品标题', max_length=60, verbose_name='标题')),
                ('sid', models.CharField(blank=True, help_text='商品货号', max_length=40, verbose_name='货号')),
            ],
            options={
                'verbose_name': '商品信息',
                'verbose_name_plural': '商品信息',
            },
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now=True, help_text='最新的更新日期', verbose_name='最新更新日期')),
                ('create', models.DateTimeField(auto_now_add=True, help_text='创建日期', verbose_name='创建日期')),
                ('title', models.CharField(help_text='订单的标题，显示的名称', max_length=100, verbose_name='订单标题')),
                ('num', models.CharField(default='2020-01-03 13:09:02', help_text='订单号，如果没有订单号的时候会默认设置成日期', max_length=100, verbose_name='订单号')),
                ('total', models.DecimalField(decimal_places=2, help_text='订单支付金额', max_digits=8, verbose_name='金额')),
            ],
            options={
                'verbose_name': '进货单',
                'verbose_name_plural': '进货单',
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now=True, help_text='最新的更新日期', verbose_name='最新更新日期')),
                ('create', models.DateTimeField(auto_now_add=True, help_text='创建日期', verbose_name='创建日期')),
                ('name', models.CharField(help_text='卖家名称', max_length=100, verbose_name='商家名称')),
                ('title', models.CharField(blank=True, help_text='卖家会员名', max_length=100, verbose_name='卖家会员名')),
            ],
            options={
                'verbose_name': '供货商',
                'verbose_name_plural': '供货商',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now=True, help_text='最新的更新日期', verbose_name='最新更新日期')),
                ('create', models.DateTimeField(auto_now_add=True, help_text='创建日期', verbose_name='创建日期')),
                ('title', models.CharField(help_text='显示的标题', max_length=30, verbose_name='标题')),
            ],
            options={
                'verbose_name': '标记',
                'verbose_name_plural': '标记',
            },
        ),
        migrations.CreateModel(
            name='PurchaseOrderPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now=True, help_text='最新的更新日期', verbose_name='最新更新日期')),
                ('create', models.DateTimeField(auto_now_add=True, help_text='创建日期', verbose_name='创建日期')),
                ('price', models.DecimalField(decimal_places=2, help_text='进货单的价格', max_digits=8, verbose_name='价格')),
                ('num', models.PositiveSmallIntegerField()),
                ('commodity', models.ForeignKey(help_text='商品的外键', on_delete=django.db.models.deletion.CASCADE, to='potato_admin.Commodity', verbose_name='商品编码')),
                ('order', models.ForeignKey(help_text='订单的外键', on_delete=django.db.models.deletion.CASCADE, to='potato_admin.PurchaseOrder', verbose_name='order 外键')),
            ],
            options={
                'verbose_name': '订单价格信息',
                'verbose_name_plural': '订单价格信息',
            },
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='seller',
            field=models.ForeignKey(blank=True, help_text='商家信息', on_delete=django.db.models.deletion.CASCADE, to='potato_admin.Seller', verbose_name='商家信息'),
        ),
        migrations.AddField(
            model_name='commodity',
            name='buy_price',
            field=models.ManyToManyField(help_text='根据订单获取买入价格', through='potato_admin.PurchaseOrderPrice', to='potato_admin.PurchaseOrder', verbose_name='买入价格'),
        ),
        migrations.AddField(
            model_name='commodity',
            name='category',
            field=models.ForeignKey(blank=True, help_text='分类描述', on_delete=django.db.models.deletion.CASCADE, to='potato_admin.Category', verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='commodity',
            name='tag',
            field=models.ManyToManyField(blank=True, help_text='标签', to='potato_admin.Tags', verbose_name='标签'),
        ),
    ]
