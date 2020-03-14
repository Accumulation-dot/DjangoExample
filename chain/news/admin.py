from django.contrib import admin

# Register your models here.
from news.models import Content, Record


@admin.register(Content)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Record)
class NewsRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'news',)
