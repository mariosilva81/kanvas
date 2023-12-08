from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request
from django.views import View


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_superuser


class IsSuperUser(BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return request.user.is_authenticated and request.user.is_superuser
