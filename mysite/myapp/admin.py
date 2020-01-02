from django.contrib import admin

from .models import *

# Register your models here.


# admin.site.register(BoughtPrice)

admin.site.register(Category)

admin.site.register(EntryOrder)

admin.site.register(SoldOrderDetails)

admin.site.register(SoldOrder)

admin.site.register(Goods)

admin.site.register(Tags)

admin.site.register(EntryOrderDetail)
