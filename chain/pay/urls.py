from django.urls import path

from pay import views as pv

urlpatterns = [
    path('list/', pv.PayView.as_view()),
    path('list/<int:pk>/', pv.PayDetailView.as_view()),
]