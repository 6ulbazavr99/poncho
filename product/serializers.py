from rest_framework import serializers

from product.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='self.request.user')

    class Meta:
        model = Product
        fields = '__all__'
