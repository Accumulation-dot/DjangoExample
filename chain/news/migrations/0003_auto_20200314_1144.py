# Generated by Django 3.0.2 on 2020-03-14 11:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0002_record_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='date',
        ),
        migrations.AddField(
            model_name='content',
            name='readers',
            field=models.ManyToManyField(related_name='readers', through='news.Record', to=settings.AUTH_USER_MODEL),
        ),
    ]
