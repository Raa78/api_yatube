"""подробнее изучить тему
https://oluchiorji.com/django-rest-framework-tutorial-permissions/
https://stackoverflow.com/questions/59141266/drf-only-author-can-create-or-update-the-book-permission
https://github.com/DistrictDataLabs/minimum-entropy/blob/master/users/permissions.py
!!! комент убрать при отправке на ревью !!!
"""
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Расширяем базовый класс "permissions.BasePermission"
    ограничиваем пользовательские разрешения.
    """
    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
