from django.contrib import admin

from myapi.model.commodity import *
from myapi.model.order import *


# Register your models here.

####


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'img_display',)
    readonly_fields = ('img_display',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_editable = ['title']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'img_display',)
    readonly_fields = ('img_display',)
    list_editable = ['title']


@admin.register(Commodity)
class CommodityAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'sub_title', 'price', 'img_display')
    readonly_fields = ('img_display',)
    list_editable = ['title', 'sub_title', 'price']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(UserOrder)
class UserOrderAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderInfo)
class OrderInfoAdmin(admin.ModelAdmin):
    pass



