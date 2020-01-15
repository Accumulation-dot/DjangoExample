from django.contrib import admin
from  .models import *
# Register your models here.

"""
@admin.register(Category1)
class Category1Admin(admin.ModelAdmin):
    list_display = ('name',)
    ordering = ('updated',)


@admin.register(Category2)
class Category2Admin(admin.ModelAdmin):
    list_display = ('name', 'parent',)
    ordering = ('updated',)


@admin.register(Category3)
class Category3Admin(admin.ModelAdmin):
    list_display = ('name', 'parent',)
    ordering = ('updated',)


@admin.register(Category4)
class Category4Admin(admin.ModelAdmin):
    list_display = ('name', 'parent',)
    ordering = ('updated',)

"""


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent',)
    ordering = ('updated',)

