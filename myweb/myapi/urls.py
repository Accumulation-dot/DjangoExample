from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework_jwt.views import refresh_jwt_token, obtain_jwt_token

from myapi.view.base import *
from myapi.view.commodity import *
from myapi.view.order import *

urlpatterns = [
    #  ...
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    # # path('register/', UserView.as_view()),
    # # path('users/', UsersView.as_view()),
    # path('commodity_list/', CommodityList.as_view()),
    # path('commodity_detail/<int:pk>/', CommodityDetail.as_view()),
    # path('category_list/', CategoryList.as_view()),
    # path('category_detail/<int:pk>/', CategoryDetail.as_view()),
    # path('tag_list/', TagList.as_view()),
    # path('tag_detail/<int:pk>/', TagDetail.as_view()),
    path('v1/', include([
        path('image_list/', ImageList.as_view()),
        path('image_detail/', ImageDetail.as_view()),
        path('tag_list/', TagList.as_view()),
        path('tag_detail/', TagDetail.as_view()),
        path('category_list/', CategoryList.as_view()),
        path('category_detail/', CategoryDetail.as_view()),
        path('seller_list/', SellerList.as_view()),
        path('seller_detail/', SellerDetail.as_view()),
        path('commodity_list/', CommodityList.as_view()),
        path('commodity_detail/', CommodityDetail.as_view()),
        path('order_list/', OrderList.as_view()),
        path('order_detail/', OrderDetail.as_view()),
        path('user_order_list/', UserOrderList.as_view()),
        path('user_order_detail/', UserOrderDetail.as_view()),
        path('order_info_list/', OrderInfoList.as_view()),
        path('order_info_detail/', OrderInfoDetail.as_view()),
    ]))


]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
