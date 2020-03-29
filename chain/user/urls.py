from django.urls import path

from user.views import UserCreation, identifier_request, login_request

# from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('register/', UserCreation.as_view()),
    # path('login/', obtain_jwt_token),
    path('login/', login_request),
    path('identify/', identifier_request),
]
