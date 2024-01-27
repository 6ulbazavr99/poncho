from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from account.models import Vendor
from account.permissions import IsAccountOwner, IsAccountOwnerOrAdmin, IsHead, IsHeadOrAdmin
from account.serializers import UserSerializer, UserListSerializer, UserProfileSerializer, \
    VendorSerializer, VendorListSerializer, VendorProfileSerializer, UserRegisterSerializer

from account.utils import send_confirmation_email


User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_permissions(self):
        if self.action in ('update', 'partial_update'):
            return [IsAccountOwner()]
        elif self.action == 'destroy':
            return [IsAccountOwnerOrAdmin()]
        return [AllowAny()]

    def get_serializer_class(self):
        if self.action == 'create':
            return UserRegisterSerializer
        elif self.action == 'list':
            return UserListSerializer
        elif self.action in ('update', 'partial_update', 'retrieve'):
            return UserProfileSerializer
        return UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if user:
            try:
                send_confirmation_email(user.email, user.activation_code)
            except Exception as e:
                return Response(
                    {'message': 'Пользователь зарегистрирован, но возникли проблемы с отправкой электронной почты!',
                     'data': serializer.data}, status=201)
        return Response({'message': 'Пользователь успешно зарегистрирован, и отправлено письмо для активации!',
                         'data': serializer.data}, status=201)

    @action(['GET'], detail=False, url_path='activate/(?P<uuid>[0-9A-Fa-f-]+)')
    def activate(self, request, uuid):
        try:
            user = User.objects.get(activation_code=uuid)
        except User.DoesNotExist:
            return Response({'message': 'Недействительная ссылка или срок действия ссылки истек!',
                             'data': {'activation_code': uuid}}, status=400)
        user.is_active = True
        user.save()
        return Response({'message': 'Аккаунт успешно активирован!', 'data': {'user_id': user.id}}, status=200)


class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def get_permissions(self):
        if self.action in ('update', 'partial_update'):
            return [IsHead()]
        elif self.action == 'destroy':
            return [IsHeadOrAdmin()]
        return [AllowAny()]

    def get_serializer_class(self):
        if self.action == 'list':
            return VendorListSerializer
        if self.action == 'retrieve':
            return VendorProfileSerializer
        return VendorSerializer

    def perform_create(self, serializer):
        serializer.save(head=self.request.user)
        vendor_instance = serializer.instance
        vendor_instance.members.add(self.request.user)
