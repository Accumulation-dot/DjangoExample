from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler

from coins.models import register_record
from user.models import CoinUser, CoinUserInfo, user_info_creation
from user.serializer import UserSerializer, CoinUserInfoSerializer

# from rest_framework_jwt.authentication import

User = get_user_model()


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CoinUser.objects.get(username=username)
            if user.check_password(password):
                print('check success')
                return user
        except Exception:
            return None


class UserCreation(generics.CreateAPIView):
    queryset = CoinUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user_info_creation(user)

        register_record(user)
        info = CoinUserInfo.objects.filter(user=user.id).first()
        info_serializer = CoinUserInfoSerializer(info)
        headers = self.get_success_headers(serializer.data)
        data = info_serializer.data

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        data['token'] = token

        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

        # def perform_create(self, serializer):
        # user = serializer.save()
        # user_info_creation(user)
        # register_record(user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# def login_action(request):
#     print(request.method)
#     if request.method == 'POST':
#         u = request.POST.get('u', '')
#         p = request.POST.get('p', '')
#         user = authenticate(username=u, password=p)
#         token = Token.objects.create(user=user)
#         return JsonResponse(data={'token': token})
#     return JsonResponse(data='不支持', status=status.HTTP_405_METHOD_NOT_ALLOWED)
