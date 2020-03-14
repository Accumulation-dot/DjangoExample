from django.contrib import admin

from user.models import CoinUserInfo
# Register your models here.

@admin.register(CoinUserInfo)
class CoinUserInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
