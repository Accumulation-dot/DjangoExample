# Generated by Django 3.0.2 on 2020-03-12 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoinGainRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin_number', models.FloatField(help_text='获取的分数', verbose_name='分数')),
                ('reason', models.CharField(help_text='获取途径', max_length=100, verbose_name='获取途径')),
                ('datetime', models.DateTimeField(auto_now=True, help_text='获取的日期时间', verbose_name='获取日期时间')),
            ],
            options={
                'verbose_name': '获取记录表',
                'verbose_name_plural': '获取记录表',
            },
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.FloatField(verbose_name='交易的数量总量')),
                ('type', models.SmallIntegerField(choices=[(1, '出售'), (2, '收购')], default=1, help_text='类型 1: 出售 2 收购', verbose_name='类型')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, '默认状态'), (1, '待付款'), (2, '取消'), (3, '完成'), (4, '删除')], default=0, help_text='状态', verbose_name='状态')),
            ],
            options={
                'verbose_name': '交易表',
                'verbose_name_plural': '交易表',
            },
        ),
        migrations.CreateModel(
            name='TradeRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now=True, help_text='交易时间', verbose_name='交易时间')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, '默认状态'), (1, '待付款'), (2, '取消'), (3, '完成'), (4, '删除')], default=1, help_text='状态', verbose_name='状态')),
            ],
            options={
                'verbose_name': '交易记录',
                'verbose_name_plural': '交易记录',
            },
        ),
    ]
