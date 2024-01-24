# class IsHeadOrAdmin(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.user.is_superuser:
#             return True
#         return request.user.id == obj.head.id
from rest_framework import permissions


class IsOwnerOrHead(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):

        print(request.user.products.all(), 'ASDLASDLASDLASD')
        print(obj.vendor.head, request.user)

        if obj in request.user.products.all():
            return True
        return obj.vendor.head == request.user
