from rest_framework.permissions import BasePermission, SAFE_METHODS
from rest_framework.request import Request
from django.views import View


class IsCourseStudentOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request: Request, view: View, obj):
        return (
            request.method in SAFE_METHODS and request.user in obj.course.students.all()
        ) or request.user.is_superuser
