from django.urls import path, include

from trade.views import sell_list, buy_list, trade_item
from trade import views
urlpatterns = [
    path('sell/', sell_list),
    path('buy/', buy_list),
    path('buy/<int:pk>/', trade_item),
    path('records/', views.records),
    path('record/<int:pk>/', views.trade_record),
    path('record/', views.trade_record_create),

]
