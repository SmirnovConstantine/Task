from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist

from .serializers import UserSerializer, RegisterSerializer, EnterSerializer
from .models import User


# Регистрация
class RegisterAPI(generics.GenericAPIView):
    """ Регистрация пользователей """
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


# Вход
class EnterAPI(generics.GenericAPIView):
    """ Вход пользователей """
    serializer_class = EnterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


# Пользователи
class UserAPI(generics.RetrieveAPIView):
    """ Просмотр пользователя """
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = UserSerializer

    def get_object(self, pk):
        # Пытаемся получить пользователя
        try:
            return User.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        # Просмотр пользователя
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)



