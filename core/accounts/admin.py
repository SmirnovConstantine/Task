from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    """ Пользователи """
    list_display = ("username", "email", "user_type", "is_superuser")


admin.site.register(User, UserAdmin)
