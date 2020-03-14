from django.contrib import admin

# Register your models here.
from chains.machine.machine import Machine, MachineRecord
from chains.news.news import News, NewsRecord


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(MachineRecord)
class MachineRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'machine',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(NewsRecord)
class NewsRecordAdmin(admin.ModelAdmin):
    list_display = ('news', 'user', 'datetime',)