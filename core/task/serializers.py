from rest_framework import serializers

from accounts.serializers import UserSerializer
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """ Сериализация заявки """
    creater = UserSerializer()

    class Meta:
        model = Task
        fields = ("creater", "date", "status")


class TaskCreateSerializer(serializers.ModelSerializer):
    """ Сериализация создания заявки """

    class Meta:
        model = Task
        fields = ("creater", )


class TaskUpdateSerializer(serializers.ModelSerializer):
    """ Сериализация обновления заявки """

    class Meta:
        model = Task
        fields = ("status", )





