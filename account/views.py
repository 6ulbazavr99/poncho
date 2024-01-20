from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from account.permissions import IsAuthenticatedUser, IsAuthenticatedUserOrAdmin
from account.serializers import RegisterSerializer, UserSerializer, UserListSerializer, UserProfileSerializer


User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_permissions(self):
        if self.action in ('update', 'partial_update'):
            return [IsAuthenticatedUser()]
        elif self.action in ('retrieve', 'destroy'):
            return [IsAuthenticatedUserOrAdmin()]
        return [AllowAny()]

    def get_serializer_class(self):
        if self.action == 'create':
            return RegisterSerializer
        elif self.action == 'list':
            return UserListSerializer
        elif self.action in ('update', 'partial_update'):
            return UserProfileSerializer
        return UserSerializer


# class VendorViewSet(viewsets.ModelViewSet):
#     queryset = Vendor.objects.all()
#     serializer_class = VendorSerializer
