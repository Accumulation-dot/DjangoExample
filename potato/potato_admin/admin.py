from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Commodity)
class CommodityAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'sid', 'price', 'category')  # 需要显示的标题
    list_per_page = 50  # 默认显示是100
    ordering = ('-create',)  # 排序
    list_editable = ['price', 'category', 'sid']  # 可编辑的字段
    fk_fields = ['category']
    list_filter = ('tag', 'category',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('title',)
    list_per_page = 10
    ordering = ('id',)


@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('title',)
    list_per_page = 30
    ordering = ('id',)


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    ordering = ('last_update',)


@admin.register(PurchaseOrderPrice)
class PurchaseOrderPriceAdmin(admin.ModelAdmin):
    list_per_page = 100
    ordering = ('-last_update',)


class OrderInline(admin.TabularInline):
    model = PurchaseOrderPrice
    extra = 0


@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    inlines = [OrderInline]
    list_display = ('id', 'title', 'num', 'seller', 'total')
    list_per_page = 100
    list_display_links = ('title', 'id')




# admin.site.register(Commodity, CommodityAdmin)
