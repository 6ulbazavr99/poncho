from rest_framework import status
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from account.models import Vendor
from product import serializers
from product.models import Category, Product
from product.permissions import IsOwnerOrHead, IsOwner, IsMembership


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer

    def get_permissions(self):
        if self.action in ('retrieve', 'list'):
            return [AllowAny()]
        else:
            return [IsAdminUser()]


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = serializers.ProductSerializer

    def get_permissions(self):
        if self.action in ('update', 'partial_update'):
            return [IsOwner()]
        elif self.action == 'create':
            return [IsAuthenticated()]
        elif self.action == 'destroy':
            return [IsOwnerOrHead()]
        return [AllowAny()]

    def create(self, request, *args, **kwargs):
        vendor_id = request.data.get('vendor')
        user = request.user

        try:
            vendor = Vendor.objects.get(id=vendor_id)
        except Vendor.DoesNotExist:
            return Response({"Ошибка": "Поставщик не найден"}, status=status.HTTP_404_NOT_FOUND)

        if user in vendor.members.all():
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(owner=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"Ошибка": "Пользователь не является членом указанного поставщика"}, status=status.HTTP_403_FORBIDDEN)
