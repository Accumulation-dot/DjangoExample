from django.urls import path

from trade import views

urlpatterns = [
    # 获取所有的出售信息
    path('sell/list/', views.sell_list),
    # 获取自己的出售信息
    path('sell/mine/', views.sell_mine),
    # 发布出售信息
    path('sell/item/', views.sell_item),

    # buy 获取所有收购信息
    path('buy/list/', views.buy_list),
    # 获取自己的收购信息
    path('buy/mine/', views.buy_mine),

    # 发布收购信息
    path('buy/item/', views.buy_item),

    path('sell/item/order/', views.sell_item_order),
    path('sell/item/confirm/', views.sell_item_confirm),


    path('buy/item/order/', views.buy_item_order),

    #
    # path('buy/<int:pk>/', trade_item),
    # path('records/', views.records),
    # path('record/<int:pk>/', views.trade_record),
    # path('record/', views.trade_record_create),
    # path('record/fill/', views.trade_record_fill),
    # path('record/confirm/', views.item_code)
]
