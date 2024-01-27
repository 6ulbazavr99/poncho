from rest_framework import status
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from account.models import Vendor
from product import serializers
from product.models import Category, Product
from product.permissions import IsOwnerOrHead, IsOwner
from product.serializers import ProductListSerializer, ProductProfileSerializer, ProductSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()

    def get_permissions(self):
        if self.action in ('retrieve', 'list'):
            return [AllowAny()]
        return [IsAdminUser()]

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.CategoryListSerializer
        return serializers.CategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()

    def get_permissions(self):
        if self.action in ('update', 'partial_update'):
            return [IsOwner()]
        elif self.action == 'create':
            return [IsAuthenticated()]
        elif self.action == 'destroy':
            return [IsOwnerOrHead()]
        return [AllowAny()]

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        # elif self.action in ('retrieve', 'partial_update', 'update'):
        #     return ProductProfileSerializer
        return ProductSerializer

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
