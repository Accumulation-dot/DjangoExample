from django.urls import path
from advert import views
from advert.views import user_records

urlpatterns = [
    path('list/', views.ContentView.as_view()),
    path('list/<int:pk>/', views.ContentDetailView.as_view()),
    path('record/', views.RecordView.as_view()),
    path('record/<int:pk>/', views.RecordDetailView.as_view()),
    path('records/', user_records),
]