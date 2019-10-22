from accounts.models import User
from django.db import models


class Task(models.Model):
    """ Модель заявки """
    creater = models.ForeignKey(User, verbose_name="Создатель", on_delete=models.CASCADE, related_name="creater")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    status = models.BooleanField(verbose_name="Статус заявки", default=False)

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
