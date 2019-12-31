from django.contrib import admin

from .models import Tags, BoughtPrice, SoldPrice, Goods, Category, EntryOrder

# Register your models here.


admin.site.register(BoughtPrice)

admin.site.register(Category)

admin.site.register(EntryOrder)

admin.site.register(Goods)

admin.site.register(SoldPrice)

admin.site.register(Tags)
