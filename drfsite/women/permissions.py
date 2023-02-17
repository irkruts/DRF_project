from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermissions):
    def has_permissions(self, request, view):
        if request.methon in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user