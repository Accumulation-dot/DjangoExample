from django.urls import path

from coins import views

# NewsListView, NewsRecordView, NewsRecordInsertView, news_list

urlpatterns = [
    path('record/', views.record_list),
]
