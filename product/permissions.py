from rest_framework import permissions


class IsOwnerOrHead(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj in request.user.products.all():
            return True
        return obj.vendor.head == request.user


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj in request.user.products.all()


class IsMembership(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user in obj.vendor.members.all()
