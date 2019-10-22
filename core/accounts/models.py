from django.db import models
from django.contrib.auth.models import AbstractUser
from .const import USER_TYPE


class User(AbstractUser):
    user_type = models.CharField(max_length=3, choices=USER_TYPE, verbose_name="Тип пользователя")

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"



