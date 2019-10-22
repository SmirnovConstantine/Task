from django.core.exceptions import PermissionDenied

from accounts.models import User


class RoleUserMixin(object):
    """ Проверяет, роль пользователя """
    def dispatch(self, request, *args, **kwargs):
        if request.user.user_type != 'use':
            return PermissionDenied
        return super(RoleUserMixin, self).dispatch(request, *args, **kwargs)


class RoleManagerMixin(object):
    """ Проверяет, роль пользователя """
    def dispatch(self, request, *args, **kwargs):
        if request.user.user_type != "mng":
            raise PermissionDenied
        return super(RoleManagerMixin, self).dispatch(request, *args, **kwargs)


