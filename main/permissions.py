from rest_framework import permissions

from main.choices import MEMBER, MANAGER, STUDENT, ADMIN




class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return perform_check(request, ADMIN)


class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        return perform_check(request, STUDENT)

class IsManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return perform_check(request, MANAGER)


class IsMember(permissions.BasePermission):
    def has_permission(self, request, view):
        return perform_check(request, MEMBER)


def perform_check(request, role):
    if not request.user.is_authenticated:
        return False
    return request.user.role == role
