from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from user.views import UserCreation

urlpatterns = [
    path('register/', UserCreation.as_view()),
    path('login/', obtain_jwt_token),
]
