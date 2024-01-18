from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from account.permissions import IsAuthenticatedUser, IsAuthenticatedUserOrAdmin
from account.serializers import RegisterSerializer, UserSerializer, UserListSerializer, UserProfileSerializer

User = get_user_model()


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    # def get_permissions(self):
    #     if self.action == 'list':
    #         return [AllowAny()]
    #     if self.action in ('update', 'partial_update'):
    #         return [IsAuthenticatedUser()]
    #     elif self.action in ('retrieve', 'destroy'):
    #         return [IsAuthenticatedUserOrAdmin()]
    #     return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.action == 'create':
            return RegisterSerializer
        elif self.action == 'list':
            return UserListSerializer
        elif self.action in ('update', 'partial_update'):
            return UserProfileSerializer
        return UserSerializer

