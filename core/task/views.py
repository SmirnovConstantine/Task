from rest_framework import generics, permissions
from rest_framework.response import Response
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist
from rest_framework_swagger import renderers
from rest_framework.schemas import SchemaGenerator
from rest_framework.views import APIView

from .serializers import TaskSerializer, TaskUpdateSerializer, TaskCreateSerializer
from .models import Task
from .utils import RoleManagerMixin, RoleUserMixin


# Создание заявок
class TaskCreateViewAPI(RoleUserMixin, generics.GenericAPIView):
    """ Создание заявки """
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = TaskCreateSerializer


    def post(self, request, *args, **kwargs):
        """ Сохранение заявки """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        task = serializer.save()
        return Response({"data": TaskSerializer(task, context=self.get_serializer_context()).data})


# Список всех заявок
class TaskAllViewsAPI(generics.GenericAPIView):
    """ Заявки """
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = TaskSerializer

    def get(self, request):
        """ Получение списка всех заявок """
        # Получаем данные из модели Task
        task = Task.objects.all()
        serializer = TaskSerializer(task, many=True)
        return Response({"data": serializer.data})


# Подтверждение заявки
class TaskUpdateViewsAPI(RoleManagerMixin, generics.GenericAPIView):
    """ Изменение статуса заявки. """
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = TaskUpdateSerializer

    def get_queryset(self, pk):
        """ Возвращает заявку. """
        try:
            return Task.objects.get(pk=pk)
        except ObjectDoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """ Просмотр выбранной заявки """
        task = self.get_queryset(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        """ Изменение статуса заявки """
        task = self.get_queryset(pk)
        serializer = self.get_serializer(task, data=request.data)
        serializer.is_valid(raise_exception=True)
        task = serializer.save()
        return Response({"data": TaskSerializer(task, context=self.get_serializer_context()).data})



