# Generated by Django 3.0.2 on 2020-03-14 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='record',
            options={'ordering': ['id'], 'verbose_name': '新闻表', 'verbose_name_plural': '新闻表'},
        ),
        migrations.AddField(
            model_name='record',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]