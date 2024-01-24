from rest_framework import status
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from account.models import Vendor
from product import serializers
from product.models import Category, Product


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
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"Ошибка": "Пользователь не является членом указанного поставщика"}, status=status.HTTP_403_FORBIDDEN)

    #######

    # def perform_create(self, serializer):
    #     vendors_memberships = self.request.user.vendors_members.all()
    #     print(vendors_memberships)
    #     print(self.request.user.vendors_members, '!#!@#@!#@!EASKDKSKFASFKASKF')
    #     serializer.save(vendor=self.request.user.vendors)
        # vendor_instance = serializer.instance
        # vendor_instance.members.add(self.request.user)