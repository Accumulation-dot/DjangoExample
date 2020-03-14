# Generated by Django 3.0.1 on 2020-01-03 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('potato_admin', '0003_auto_20200103_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commodity',
            name='buy_price',
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='commodities',
            field=models.ManyToManyField(through='potato_admin.PurchaseOrderPrice', to='potato_admin.Commodity'),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='num',
            field=models.CharField(default='2020-01-03 18:38:31', help_text='订单号，如果没有订单号的时候会默认设置成日期', max_length=100, verbose_name='订单号'),
        ),
    ]
