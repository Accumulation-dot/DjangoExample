from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler, JSONWebTokenSerializer

from coins.models import query_award
from user import models as um, serializers as us
from user.models import CoinUser, CoinUserInfo, user_info_creation
from user.serializers import UserSerializer, CoinUserInfoSerializer

# from rest_framework_jwt.authentication import

User = get_user_model()


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CoinUser.objects.get(username=username)
            if user.check_password(password):
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

        award_key = request.META.get('HTTP_AWARD')

        query_award(award_key, user=user)
        info = CoinUserInfo.objects.filter(user=user.id).first()
        info_serializer = CoinUserInfoSerializer(info)
        headers = self.get_success_headers(serializer.data)
        data = info_serializer.data

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        data['token'] = token

        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


@api_view(['POST'])
@permission_classes([permissions.AllowAny, ])
def login_request(request, format=None):
    seria = JSONWebTokenSerializer(data=request.data)
    seria.is_valid(raise_exception=True)
    user = seria.object.get('user')
    if user is None:
        return Response('', status=status.HTTP_404_NOT_FOUND)
    token = seria.object.get('token')
    info = CoinUserInfo.objects.filter(user=user.id).first()
    response_data = CoinUserInfoSerializer(info).data
    response_data['token'] = token
    return Response(response_data)


@api_view(['GET', 'POST'])
@permission_classes([permissions.IsAuthenticated, ])
def identifier_request(request, format=None):
    user = request.user
    identifier = um.Identifier.objects.filter(user=user).first()
    if request.method == 'GET':
        if identifier is None:
            return Response('还没有进行验证', status=status.HTTP_404_NOT_FOUND)
        return Response(us.IdentifierSerializer(identifier).data, status=status.HTTP_200_OK)
    else:
        if identifier:
            return Response('已验证', status=status.HTTP_400_BAD_REQUEST)
        ids = us.IdentifierSerializer(data=request.data)
        ids.is_valid(raise_exception=True)
        ids.save(user=user)
        return Response(ids.data, status=status.HTTP_201_CREATED)
