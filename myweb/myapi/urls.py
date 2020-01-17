from django.urls import path
from rest_framework_jwt.views import refresh_jwt_token, obtain_jwt_token
from myapi.view.order import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #  ...
    path('api-token-auth/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    # path('register/', UserView.as_view()),
    # path('users/', UsersView.as_view()),
    path('commodity_list/', CommodityList.as_view()),
    path('commodity_detail/<int:pk>/', CommodityDetail.as_view()),
    path('category_list/', CategoryList.as_view()),
    path('category_detail/<int:pk>/', CategoryDetail.as_view()),
    path('tag_list/', TagList.as_view()),
    path('tag_detail/<int:pk>/', TagDetail.as_view()),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
