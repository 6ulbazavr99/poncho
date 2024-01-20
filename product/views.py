from rest_framework.viewsets import ModelViewSet

from product import serializers
from product.models import Category


# Create your views here.


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer

    # def get_permissions(self):
    #     if self.action in ('retrieve', 'list'):
    #         return [permissions.AllowAny()]
    #     else:
    #         return [permissions.IsAdminUser()]
