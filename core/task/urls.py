from django.urls import path

from .views import TaskAllViewsAPI, TaskUpdateViewsAPI, TaskCreateViewAPI

urlpatterns = [
    path('task/create/', TaskCreateViewAPI.as_view(), name="task_create"),
    path('task/all/', TaskAllViewsAPI.as_view(), name="all_task"),
    path('task/<int:pk>/', TaskUpdateViewsAPI.as_view(), name="task_update"),
]
