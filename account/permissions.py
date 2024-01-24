from rest_framework import permissions


class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.id


class IsAccountOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return request.user.id == obj.id


class IsHead(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.id == obj.head.id


class IsHeadOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True
        return request.user.id == obj.head.id
