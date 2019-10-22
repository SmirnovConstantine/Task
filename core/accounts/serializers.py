from rest_framework import serializers
from .models import User
from django.contrib.auth import authenticate


# Ползователи
class UserSerializer(serializers.ModelSerializer):
    """ Сериализация пользоваетлей """
    class Meta:
        model = User
        fields = ("id", "username", "email", "user_type")


# Регистрация пользователя
class RegisterSerializer(serializers.ModelSerializer):
    """ Сериализация регистрации пользователей """
    class Meta:
        model = User
        fields = ("id", "username", "email", "password", "user_type")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        # Функция создания пользователя
        user_type = {"user_type": validated_data["user_type"]}
        user = User.objects.create_user(validated_data["username"],
                                        validated_data["email"],
                                        validated_data["password"],
                                        **user_type)
        return user


# Вход пользователя
class EnterSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user.is_active:
            return user
        else:
            raise serializers.ValidationError("Incorrect Candidates")
